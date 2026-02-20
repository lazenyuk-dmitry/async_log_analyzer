import asyncio
from typing import List, Set
from app.models.log_entry import LogEntry
from app.utils.benchmark import benchmark

class LogService:
    def __init__(self, logs: List[LogEntry]):
        self.logs = logs

    @benchmark
    async def get_unique_ips_slow(self) -> List[str]:
        """Сложность O(n²) — крайне медленно на больших данных."""
        unique_ips = []
        for log in self.logs:
            # Операция 'in' для списка имеет сложность O(n)
            # Внутри цикла это дает n * n = O(n²)
            if log.ip not in unique_ips:
                unique_ips.append(log.ip)
        return unique_ips

    @benchmark
    async def get_unique_ips_fast(self) -> Set[str]:
        """Сложность O(n) — идиоматичный Python."""
        # Создание set из итератора проходит по списку 1 раз.
        # Хеширование в set дает поиск за O(1).
        return {log.ip for log in self.logs}
