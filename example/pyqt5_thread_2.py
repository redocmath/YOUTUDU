# 많이 사용
import threading


class Thread_run(threading.Thread):
    def run(self):
        print('Thread running Class')


for i in range(1000):
    t = Thread_run()
    t.start()
