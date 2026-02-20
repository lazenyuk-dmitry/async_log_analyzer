import asyncio
import random
from datetime import datetime
from app.models.log_entry import LogEntry
from app.services.log_service import LogService

async def main():
    # Генерируем тестовые данные
    print("Генерация данных...")
    test_logs = [
        LogEntry(
            timestamp=datetime.now(),
            level="INFO",
            ip=f"192.168.1.{random.randint(1, 1000)}",
            response_time=random.random()
        ) for _ in range(50000) # range
    ]

    log_service = LogService(test_logs)

    print("\n--- Запуск поиска (Медленный метод O(n²)) ---")
    await log_service.get_unique_ips_slow()

    print("\n--- Запуск поиска (Быстрый метод O(n)) ---")
    await log_service.get_unique_ips_fast()

if __name__ == "__main__":
    asyncio.run(main())
