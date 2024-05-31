from environs import Env

env = Env()
env.read_env()


class DataSender:
    def __init__(self):
        self.storage_type = env("STORAGE_TYPE")

    async def send(self, aggregated_data):
        if self.storage_type == "kafka":
            await self.send_to_kafka(aggregated_data)
        elif self.storage_type == "postgres":
            await self.send_to_postgres(aggregated_data)

    async def send_to_kafka(self, aggregated_data):
        """ Здесь реализация отправки в Kafka """
        pass

    async def send_to_postgres(self, aggregated_data):
        """Здесь реализация отправки в PostgreSQL"""
        pass
