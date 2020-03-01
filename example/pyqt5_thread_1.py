import threading


def thread_run():
    print('Thread run! in Function')


def thread_run_msg(msg):
    print('Thread run! in Function - %s' % msg)


for i in range(1000):
    t1 = threading.Thread(target=thread_run)
    t2 = threading.Thread(target=thread_run_msg, args=('service', ))

    t1.start()
    t2.start()
