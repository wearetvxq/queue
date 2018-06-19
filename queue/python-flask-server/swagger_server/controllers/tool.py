from RedisQueue import RedisQueue
import time,os



#时间变成字符串(文件夹)
def utc_timestamp_to_str(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y%m%d", timeArray)
    return otherStyleTime

#时间变成字符串(文件名)
def utc_timestamp_to_str_file(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y%m%d%H%M%S", timeArray)
    return otherStyleTime






#-------------参数的定义-----------------------------------#
#redis数据库名                                             #
redisname='chengda'                                       #
#获取原始图片地址                                           #
url_dir_name='/home/user/桌面/20180604/'                  #
#保存图片时，文件夹名                                       #
dir_name=utc_timestamp_to_str(int(time.time()))          #
#保存图片路径                                              #
dir_path='/var/www/downfile/chibipic'                    #
#拼接成完整地址                                            #
save_path='{}/{}'.format(dir_path,dir_name)              #
#------------参数的定义-----------------------------------#

# 写入redis以及对应文件夹下生成对应图片（暂时没有对识别人脸判断，需判断，只写入人脸）
def import_pic(redisname,url,save_path):
    #读取图片（二进制）
    f=open(r'{}'.format(url),"rb") #二进制方式打开图文件
    base64_data=f.read()
    filename=f.name.split('/')[-1]
    f.close()




    jzh=RedisQueue(name='{}'.format(redisname))
    #写入数据
    jzh.put({"pic":base64_data})


    #获取数据------这里应该是yoran调用，我这边判断返回值及
    value=eval(jzh.get())

    # 根据yoran算法，如果照片中有人脸的话。保存图片
    if jzh:
        #name = utc_timestamp_to_str_file(int(time.time()))
        try:
            f = open(r'{}/{}'.format(save_path, filename), 'wb')

        except:
            os.mkdir(save_path)
            f = open(r'{}/{}'.format(save_path, filename), 'wb')
        f.write(value['pic'])
        f.close()
#遍历文件文件夹下的图片
while (1):
    for filename in os.listdir(r"{}".format(url_dir_name)):
        url = url_dir_name + filename
        print(url)
        # time.sleep(1)
        import_pic(redisname, url, save_path)
        os.remove(url)
        print('已删除图片：-----',filename)