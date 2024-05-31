
from typing import Union, List, Dict
from collections import defaultdict
import time
from environs import Env
from vabus import Event


env = Env()
env.read_env()


AGGREGATION_TIME_WINDOW = env.int("AGGREGATION_TIME_WINDOW")


class EventAggregator:
    def __init__(self):
        # Словарь для хранения событий, группированных по имени и функции агрегации
        self.events = defaultdict(list)
        # Словарь для хранения времени последней агрегации для каждой группы
        self.last_aggregation_time = defaultdict(lambda: time.time())

    def add_event(self, event: Event):
        """Добавляет событие в буфер агрегации группируя события
        по ключу (имя события, функция агрегации)"""
        key = (event.name, event.agg_func)
        self.events[key].append(event)

    def aggregate(self) -> List[Dict]:
        """
        Выполняет агрегацию событий на основе названия, функции и временного окна.
        """
        current_time = time.time()
        aggregated_data = []

        for key, events in self.events.items():
            name, agg_func = key
            # Проверка, достаточно ли времени прошло с последней агрегации
            if current_time - self.last_aggregation_time[key] >= AGGREGATION_TIME_WINDOW:
                # Если да, выполняем агрегацию
                aggregated_value = self.compute_aggregated_value(
                    events, agg_func)
                aggregated_data.append({
                    'name': name,
                    'function': agg_func,
                    'value': aggregated_value
                })
                # Сбрасываем записи для ключа после выполнения агрегации
                self.events[key] = []
                # Обновляем время последней агрегации для этого ключа
                self.last_aggregation_time[key] = current_time

        return aggregated_data

    def compute_aggregated_value(self, events: List[Event], agg_func: str) -> Union[int, float]:
        """Агрегированние в зависимости от функции."""
        if agg_func == "sum":
            computed_value = self.aggregate_sum(events)
        elif agg_func == "avg":
            computed_value = self.aggregate_avg(events)
        elif agg_func == "min":
            computed_value = self.aggregate_min(events)
        elif agg_func == "max":
            computed_value = self.aggregate_max(events)
        else:
            raise NotImplementedError(f"""Aggregation function {
                                      agg_func} is not implemented.""")
        return computed_value

    def aggregate_sum(self, events: List[Event]) -> Union[int, float]:
        """Агрегация суммы значений."""
        pass

    def aggregate_avg(self, events: Event) -> Union[int, float]:
        """Агрегация среднего значения."""
        pass

    def aggregate_min(self, events: Event) -> Union[int, float]:
        """Агрегация минимального значения."""
        pass

    def aggregate_max(self, events: Event) -> Union[int, float]:
        """Агрегация максимального значения."""
        pass
