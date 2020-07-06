from threading import*
from time import sleep

class hello(Thread):
 def run(self):
   for i in range(0,10):
    print("hello")
 sleep(1)

class hi(Thread):
 def run(self):
   for i in range(0,10):
    print("hi")
 sleep(1)
	
t1 = hello()
t2 = hi()

t1.start()
sleep(0.2)
t2.start()
t2.join()
print("bye")
