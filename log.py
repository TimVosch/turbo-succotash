from fluent import sender, event
import time, random, timeit

sender.setup('poc', host='127.0.0.1', port=24224)
while True:
    event.Event('Export', {
        'size': random.randrange(0, 10000000),
        'user': 'tim.vanosch'
    })
    print(".")
    time.sleep(0.8)
    
sender.close()

# Shell command (ran in pipenv) to measure send function execution time. Avg. 30-50 usec
# python -m timeit -s 'from fluent import sender, event; sender.setup("poc", host="127.0.0.1", port=24224)' 'event.Event("test", {"test": 1})'