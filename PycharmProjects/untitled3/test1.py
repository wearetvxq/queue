#fname=input('Enter filename:')
import time
print (time.asctime( time.localtime(time.time()) ))
print('开始')
try:
    fobj=open('j','a')                 # 这里的a意思是追加，这样在加了之后就不会覆盖掉源文件中的内容，如果是w则会覆盖。
except IOError:
    print ('*** file open error:')
else:
    fobj.write('\n'+'fangangnang'+time.asctime( time.localtime(time.time()) ))   #  这里的\n的意思是在源文件末尾换行，即新加内容另起一行插入。
    fobj.close()                              #   特别注意文件操作完毕后要close
print('结束')