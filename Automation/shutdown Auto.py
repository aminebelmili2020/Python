import os
import time as t
cur=t.strftime("%H:%M")
print (cur)
set_time=str(input("Enter The Shutdown Time: "))
print("Shutdown Time is ",set_time)
while True:
  current=t.strftime("%H:%M")
  if set_time==current:
    os.system("shutdown /s /t 1")
    exit()
  else:
    t.sleep(10)