import multiprocessing
import time

###############################################
# 並列処理のサンプル
# 2つのプロセスを立ち上げ、それぞれで異なる処理を行う
###############################################


def print_time_elapsed():
    """プロセス内で経過時間を表示する関数"""
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}秒です")
        time.sleep(1)


def print_process_running():
    """プロセス内で動作中であることを表示する関数"""
    while True:
        print("プロセスは動作しています")
        time.sleep(5)


if __name__ == "__main__":
    # プロセスを2つ立ち上げる
    process1 = multiprocessing.Process(target=print_time_elapsed)
    process2 = multiprocessing.Process(target=print_process_running)

    # プロセスを開始する
    process1.start()
    process2.start()

    # プロセスが終了するまで待つ
    process1.join()
    process2.join()
