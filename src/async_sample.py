###############################################
# 非同期処理のサンプル
# 同期処理と非同期処理の処理時間を比較する
###############################################

import asyncio
import logging
import time

from tqdm import tqdm

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def wait_one_second(wait_time: int):
    """wait_time秒待つ"""
    time.sleep(wait_time)


async def wait_one_second_async(wait_time: int):
    """wait_time秒待つ
    非同期処理用
    """
    await asyncio.sleep(wait_time)


# 同期処理
def sync_main() -> float:
    """
    同期処理で1秒待つタスクを10回する
    """
    start_time = time.perf_counter()
    for _ in tqdm(range(10), desc="Sync Main"):
        wait_one_second(1)

    process_time = time.perf_counter() - start_time
    logger.info(f"Sync Main End: {process_time} [s]")
    return process_time


# 非同期処理の書き方あれこれ
async def async_main() -> float:
    """
    非同期処理で1秒待つタスクを10回する
    シンプルに
    """
    start_time = time.perf_counter()
    # wait_one_second_async()を10回分用意して、*で展開して非同期処理を実行
    await asyncio.gather(*(wait_one_second_async(1) for _ in range(10)))

    process_time = time.perf_counter() - start_time
    logger.info(f"Async Main End: {process_time} [s]")
    return process_time


async def async_main_with_progress() -> float:
    """
    非同期処理で1秒待つタスクを10回する
    進捗表示あり
    """
    start_time = time.perf_counter()
    tasks = [wait_one_second_async(1) for _ in range(10)]
    # tqdmで進捗表示
    for f in tqdm(asyncio.as_completed(tasks), total=len(tasks), desc="Async Progress"):
        await f

    process_time = time.perf_counter() - start_time
    logger.info(f"Async Main with Progress End: {process_time} [s]")
    return process_time


async def async_main_use_tasks_list() -> float:
    """非同期処理で1秒末タスクを10回実行する
    tasksリストを使ってタスクリストを作成し、非同期実行する
    """
    start_time = time.perf_counter()

    # タスクリストを作成
    tasks = []
    for _ in range(10):
        tasks.append(wait_one_second_async(1))
    # *で展開して非同期処理を実行
    await asyncio.gather(*tasks)

    process_time = time.perf_counter() - start_time
    logger.info(f"Async Main use Tasks List End: {process_time} [s]")
    return process_time


def async_to_sync() -> float:
    """
    非同期関数を同期関数に変換する
    shapなど同期関数しか使えないライブラリを使う場合に使用する

    複数の非同期処理を同期関数内部で非同期実行するには
    それら非同期処理をまとめて非同期実行する関数を作成し、
    それを同期関数内でasyncio.run()で実行する
    """
    start_time = time.perf_counter()
    asyncio.run(async_main())

    process_time = time.perf_counter() - start_time
    logger.info(f"Async to Sync End: {process_time} [s]")
    return process_time


if __name__ == "__main__":
    sync_time = sync_main()
    print("----")
    async_time1 = asyncio.run(async_main())
    print("----")
    async_time2 = asyncio.run(async_main_with_progress())
    print("----")
    async_time3 = asyncio.run(async_main_use_tasks_list())
    print("----")
    async_time4 = async_to_sync()

    print("Sync ---")
    print(f"{sync_time} [s]")

    print("Async ---")
    print(f"{async_time1} [s]")
    print(f"{async_time2} [s]")
    print(f"{async_time3} [s]")
    print(f"{async_time4} [s]")
