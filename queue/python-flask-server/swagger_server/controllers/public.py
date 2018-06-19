# -*- coding: utf-8 -*-

from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor

# 分割数据
def data_split(num,data):
    size=len(data)
    interval=int(size/num)
    lists=[]
    for i in range(num):
        if i==num-1:
            lists.append(data[i * interval:])
        else:
            lists.append(data[i * interval:(i+1) * interval])
    return lists


# 进程池,内嵌线程池
def progress_pool(func,progress,data):
    p_executor = ProcessPoolExecutor(progress)
    p_data=data_split(4,data)
    for data in p_data:
        p_executor.submit(func,str(data))


def thread_pool(func,progress,data,priority):
    p_executor = ThreadPoolExecutor(progress)
    p_data=data_split(progress,data)
    for data in p_data:
        print(type(data))
        p_executor.submit(func,data,priority)
