import argparse
import time

import ray


@ray.remote
def print_time_elapsed():
    """スレッド/プロセス内で経過時間を表示する関数"""
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}秒です")
        time.sleep(1)


@ray.remote
def print_task_running():
    """スレッド/プロセス内で動作中であることを表示する関数"""
    while True:
        print("タスクは動作しています")
        time.sleep(5)


def main(num_cpus: int):
    """
    メイン関数。Rayを使用してタスクを実行する

    Args:
        num_cpus (int): 使用するCPUコア数
    """
    print(f"Rayを使用します (num_cpus={num_cpus})")
    ray.init(num_cpus=num_cpus)
    ray.get([print_time_elapsed.remote(), print_task_running.remote()])


if __name__ == "__main__":
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="Rayを使った並列処理のサンプルコード")
    parser.add_argument("--num_cpus", type=int, default=1, help="使用するCPUコア数を指定")
    args = parser.parse_args()

    # メイン関数の実行
    main(args.num_cpus)