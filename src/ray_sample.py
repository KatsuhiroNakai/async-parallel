import argparse
import time

import ray


@ray.remote
def wait_one_second_async(wait_time: int):
    """wait_time秒待つ
    同期処理用
    """
    time.sleep(wait_time)
    print(f"{wait_time}秒待ちました")


@ray.remote
def print_time_elapsed():
    """スレッド/プロセス内で経過時間を表示する関数"""
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}秒です")
        time.sleep(1)


@ray.remote
def print_task_running(interval_time: int):
    """スレッド/プロセス内で動作中であることを表示する関数"""
    while True:
        print("タスクは動作しています")
        time.sleep(interval_time)


def main(num_cpus: int):
    """
    メイン関数
    Rayを使用してタスクを実行する

    num_cpusで指定した数のタスクしか同時に実行されない
    例えばnum_cpus = 1の場合は同期実行と同じ

    Args:
        num_cpus (int): 使用するCPUコア数
    """
    print(f"Rayを使用します (num_cpus={num_cpus})")
    ray.init(num_cpus=num_cpus)

    # 1秒で終わるタスクを並列で5つ実行
    tasks = [wait_one_second_async.remote(1) for _ in range(5)]
    ray.get(tasks)  # 並列処理の終了を待ち合わせる

    # 並列（終了を待ち合わせない）
    print_time_elapsed.remote()
    print_task_running.remote(interval_time=5)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("メインスレッドを終了します")


if __name__ == "__main__":
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="Rayを使った並列処理のサンプルコード")
    parser.add_argument("--num_cpus", type=int, default=1, help="使用するCPUコア数を指定")
    args = parser.parse_args()

    # メイン関数の実行
    main(args.num_cpus)
