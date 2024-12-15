import argparse
import concurrent.futures
import time


def print_time_elapsed():
    """スレッド/プロセス内で経過時間を表示する関数"""
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}秒です")
        time.sleep(1)


def print_task_running():
    """スレッド/プロセス内で動作中であることを表示する関数"""
    while True:
        print("タスクは動作しています")
        time.sleep(5)


def main(use_multiprocessing):
    """メイン関数。マルチスレッドまたはマルチプロセスを使用してタスクを実行する"""
    if use_multiprocessing:
        print("マルチプロセスを使用します")
        with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
            executor.submit(print_time_elapsed)
            executor.submit(print_task_running)
    else:
        print("マルチスレッドを使用します")
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            executor.submit(print_time_elapsed)
            executor.submit(print_task_running)


if __name__ == "__main__":
    # コマンドライン引数の解析
    parser = argparse.ArgumentParser(description="マルチスレッドとマルチプロセスを使い分けるサンプルコード")
    parser.add_argument(
        "--multiprocessing", action="store_true", help="マルチプロセスを使用する場合に指定, デフォルトはマルチスレッド"
    )
    args = parser.parse_args()

    # メイン関数の実行
    main(args.multiprocessing)
