import time
import random
import sys
from tqdm import tqdm
from datetime import datetime
import logging
from typing import List, Dict
import os

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('download.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class DownloadManager:
    def __init__(self):
        self.total_size = 1024 * 1024 * 2300 # 1 GB
        self.chunk_size = 1024 * 1024 * 10  # 1 MB
        self.download_speed = random.uniform(11.1, 11.3)  # MB/s (медленная скорость)
        self.files: List[Dict] = [
            {"name": "main_package.zip", "size": 4500 * 1024 * 1024},  # 450 MB
            {"name": "dependencies.tar.gz", "size": 2500 * 1024 * 1024},  # 250 MB
            {"name": "resources.bundle", "size": 300 * 1024 * 1024}  # 300 MB
        ]

    def simulate_network_delay(self):
        """Имитация сетевой задержки"""
        time.sleep(random.uniform(0.5, 1.0))  # Увеличенная задержка

    def format_size(self, size_bytes: int) -> str:
        """Форматирование размера в читаемый вид"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
        return f"{size_bytes:.2f} TB"

    def download_file(self, file_info: Dict):
        """Имитация загрузки файла"""
        file_size = file_info["size"]
        chunks = file_size // self.chunk_size
        
        logging.info(f"Начало загрузки: {file_info['name']}")
        logging.info(f"Размер файла: {self.format_size(file_size)}")
        
        with tqdm(total=chunks, desc=file_info['name'], unit='chunk') as pbar:
            for _ in range(chunks):
                self.simulate_network_delay()
                pbar.update(1)
                pbar.set_postfix({
                    'speed': f"{self.download_speed:.2f} MB/s",
                    'eta': f"{pbar.format_dict['elapsed']:.1f}s"
                })

    def verify_download(self, file_info: Dict):
        """Имитация проверки загруженного файла"""
        logging.info(f"Проверка целостности: {file_info['name']}")
        time.sleep(random.uniform(2.0, 3.0))  # Увеличенное время проверки
        if random.random() < 0.95:  # 95% шанс успешной проверки
            logging.info(f"✓ Проверка пройдена успешно: {file_info['name']}")
        else:
            logging.warning(f"! Требуется повторная загрузка: {file_info['name']}")
            self.download_file(file_info)

    def run(self):
        """Основной процесс загрузки"""
        start_time = datetime.now()
        logging.info("=== Начало процесса загрузки ===")
        
        for file_info in self.files:
            try:
                self.download_file(file_info)
                self.verify_download(file_info)
            except Exception as e:
                logging.error(f"Ошибка при загрузке {file_info['name']}: {str(e)}")
                continue

        end_time = datetime.now()
        duration = (end_time - start_time).total_seconds()
        logging.info(f"=== Загрузка завершена за {duration:.2f} секунд ===")

if __name__ == "__main__":
    downloader = DownloadManager()
    downloader.run() 