from swagger_server.controllers.RedisQueue import RedisQueue
import time

redisname='chengda'
url='/home/user/桌面/5b0688a7N4c1817e2.jpg'
save_path='/var/www/downfile/chibipic'

def import_pic(redisname,url,save_path):
    #读取图片（二进制）
    f=open(r'{}'.format(url),"rb") #二进制方式打开图文件
    base64_data=f.read()
    f.close()
    #保存图片
    name=str(int(time.time()))
    f = open(r'{}/{}.jpg'.format(save_path,name),'wb')
    f.write(base64_data)
    f.close()
    jzh=RedisQueue(name='{}'.format(redisname))
    jzh.put({"pic":base64_data})
    value=eval(jzh.get())
    print((value['pic']))
import_pic(redisname,url,save_path)