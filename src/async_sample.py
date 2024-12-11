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
    logger.info(f"Sync Main End: {time.perf_counter() - start_time} [s]")


async def async_main():
    """非同期処理で1秒待つタスクを10回する"""
    start_time = time.perf_counter()
    await asyncio.gather(*(wait_one_second_async() for _ in range(10)))
    logger.info(f"Async Main End: {time.perf_counter() - start_time} [s]")


async def async_main_with_progress():
    """
    非同期処理で1秒待つタスクを10回する
    進捗表示あり
    """
    start_time = time.perf_counter()
    tasks = [wait_one_second_async() for _ in range(10)]
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Async Progress"):
        await f
    logger.info(f"Async Main with Progress End: {time.perf_counter() - start_time} [s]")


async def async_main_use_tasks_list():
    """非同期処理で1秒末タスクを10回実行する
    tasksリストを使ってタスクリストを作成し、非同期実行する
    """
    start_time = time.perf_counter()
    tasks = []
    for _ in range(10):
        tasks.append(wait_one_second_async())

    await asyncio.gather(*tasks)
    logger.info(f"Async Main use Tasks List End: {time.perf_counter() - start_time} [s]")


def async_to_sync():
    """
    非同期関数を同期関数に変換する
    shapなど同期関数しか使えないライブラリを使う場合に使用する
    """
    start_time = time.perf_counter()
    asyncio.run(async_main())
    logger.info(f"Async to Sync End: {time.perf_counter() - start_time} [s]")


if __name__ == "__main__":
    sync_main()
    print("----")
    asyncio.run(async_main())
    print("----")
    asyncio.run(async_main_with_progress())
    print("----")
    asyncio.run(async_main_use_tasks_list())
    print("----")
    async_to_sync()
