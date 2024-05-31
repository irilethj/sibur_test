import time
from vabus import Metric


class MetricsCollector:
    def __init__(self):
        pass

    def number_of_events_processed(self):
        """Количество обработанных событий"""
        pass

    def total_uptime(self):
        """Общее количество без отказной работы"""
        pass

    def event_processing_error(self):
        """Количество ошибок обработки событий"""
        pass

    def get_memory_usage(self):
        """Использование памяти"""
        pass

    def get_metrics(self):
        metrics = [
            Metric(name="number_of_events_processed",
                   value=self.number_of_events_processed()),
            Metric(name="total_uptime",
                   value=self.total_uptime()),
            Metric(name="event_processing_error",
                   value=self.event_processing_error()),
            Metric(name="memory_usage", value=self.get_memory_usage()),
        ]
        return metrics
