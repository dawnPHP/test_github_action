import time
import random

num=random.randint(0,9)
flag=num>3

timsString=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime())
print(timsString)

if (flag):
	print(flag)
	fa = open(r"test.txt", "a")
	fa.write( str(time.time()) +":\t"+ timsString + "\n" )
	fa.close()
else:
	print("--")
