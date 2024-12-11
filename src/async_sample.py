import asyncio
import logging
import time

from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def wait_one_second():
    time.sleep(1)


async def wait_one_second_async():
    await asyncio.sleep(1)


def sync_main():
    """同期処理で1秒待つタスクを10回する"""
    start_time = time.perf_counter()
    for _ in tqdm(range(10), desc="Sync Main"):
        wait_one_second()
    logger.info(f"= Sync Main End: {time.perf_counter() - start_time} [s] =")


async def async_main():
    """非同期処理で1秒待つタスクを10回する"""
    start_time = time.perf_counter()
    tasks = [wait_one_second_async() for _ in range(10)]
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Async Progress"):
        await f
    logger.info(f"= Async Main End: {time.perf_counter() - start_time} [s] =")


if __name__ == "__main__":
    sync_main()
    asyncio.run(async_main())
