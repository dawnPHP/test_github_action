import time

fa = open(r"test.txt", "a")

timsString=time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()) 
fa.write( str(time.time()) +":\t"+ timsString + "\n" )

fa.close()
