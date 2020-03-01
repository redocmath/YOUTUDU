# 일정 시간 반복
import threading
import time


def thread_run():
    print('=====', time.ctime(), '=====')
    # 개발 코드
    for i in range(1, 1000 + 1):
        print('Thread run - f')
    threading.Timer(2.5, thread_run).start()    # 재귀


thread_run()

