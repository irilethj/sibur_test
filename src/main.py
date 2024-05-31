from environs import Env
from vabus import VaBus
import asyncio
from metrics_collector import MetricsCollector
from event_aggregator import EventAggregator
from data_sender import DataSender


env = Env()
env.read_env()


async def main():
    vabus_url = env.str("VABUS_URL")
    async with VaBus(vabus_url) as va_bus:
        aggregator = EventAggregator()
        data_sender = DataSender()
        metrics_collector = MetricsCollector()

        while True:
            print("Получение событий")
            await asyncio.sleep(1)
            event = await va_bus.get_event()
            aggregator.add_event(event)
            print("Агрегирование данных")
            aggregated_data_list = aggregator.aggregate()

            print("Отправление агрегированных данных во внешнее хранилище")
            await asyncio.sleep(1)
            for data in aggregated_data_list:
                await data_sender.send(data)

            print("Сбор метрик")
            metrics_data = metrics_collector.get_metrics()
            print("Отправление метрик в шину VaBus")
            for metric in metrics_data:
                await va_bus.send_metric(metric)

            await asyncio.sleep(2)

if __name__ == "__main__":
    asyncio.run(main())
