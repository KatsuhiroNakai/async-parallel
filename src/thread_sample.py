###############################################
# 並列処理のサンプル
# 2つのスレッドを立ち上げ、それぞれで異なる処理を行う
###############################################

import threading
import time


def print_time_elapsed():
    """スレッド内で経過時間を表示する関数"""
    start_time = time.time()
    while True:
        elapsed_time = int(time.time() - start_time)
        print(f"{elapsed_time}秒です")
        time.sleep(1)


def print_thread_running():
    """スレッド内で動作中であることを表示する関数"""
    while True:
        print("スレッドは動作しています")
        time.sleep(5)


if __name__ == "__main__":
    # スレッドを2つ立ち上げる
    thread1 = threading.Thread(target=print_time_elapsed)
    thread2 = threading.Thread(target=print_thread_running)

    # スレッドを開始する
    thread1.start()
    thread2.start()

    # スレッドが終了するまで待つ
    # NOTE: 2つまとめてjoinしないと、
    thread1.join()
    thread2.join()
