import peewee,json
from mysql_check import *
import time,random,hashlib
from hashlib import sha1
# 字符串变为时间戳
def utc_str_to_timestamp(dt):
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    # 转换成时间戳
    timestamp = time.mktime(timeArray)
    return (int(timestamp))

# 时间戳变为字符串
def utc_timestamp_to_str(dt):
    # 时间戳变成字符串
    timeArray = time.localtime(dt)
    otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    return otherStyleTime


# 根据id获取姓名
def  get_id_for_name(id):
    username=FSysEmployee.select().where(FSysEmployee.id==id).get().username
    return username

#根据姓名获取id
def  get_name_for_id(name):
    id=FSysEmployee.select().where(FSysEmployee.username==name).get().id
    return id

# 获取状态类型
def get_status_type(status):
    if status=='正常':
        type=0
    if status=='迟到':
        type = 1
    if status=='脱岗':
        type =2
    if status=='早退':
        type =3
    if status=='缺勤':
        type =4
    if status=='积极':
        type =5
    return type


    # 获取考勤时间

# 获取考勤时间
def definition_time():
    worktime=FSysAttendance.select()
# 上午
    #print('m_startwork------',json.loads(worktime[0].content)['startwork'])
    m_startwork=json.loads(worktime[0].content)['startwork']
    #print('m_startwork_late-------', json.loads(worktime[0].content)['startwork'][0:3]+json.loads(worktime[0].content)['startwork_late']+json.loads(worktime[0].content)['startwork'][5:])
    m_startwork_late=json.loads(worktime[0].content)['startwork'][0:3]+json.loads(worktime[0].content)['startwork_late']+json.loads(worktime[0].content)['startwork'][5:]
    #print('m_endwork------', json.loads(worktime[0].content)['endwork'])
    m_endwork = json.loads(worktime[0].content)['endwork']
    #print('m_endwork_late-------',json.loads(worktime[0].content)['endwork'][0:3] + json.loads(worktime[0].content)['endwork_late'] + json.loads(worktime[0].content)['endwork'][5:])
    if int(json.loads(worktime[0].content)['endwork'][3:5])-int(json.loads(worktime[0].content)['endwork_late'])<0:
        m_endwork_late = str(int(json.loads(worktime[0].content)['endwork'][0:2])-1)+':' + str((60+int(json.loads(worktime[0].content)['endwork'][3:5])-int(json.loads(worktime[0].content)['endwork_late']))) + json.loads(worktime[0].content)['endwork'][5:]
    if int(json.loads(worktime[0].content)['endwork'][3:5]) - int(json.loads(worktime[0].content)['endwork_late']) >= 0:
        m_endwork_late = json.loads(worktime[0].content)['endwork'][0:3] + str(int(json.loads(worktime[0].content)['endwork'][3:5]) - int(json.loads(worktime[0].content)['endwork_late']))  + json.loads(worktime[0].content)['endwork'][5:]

# 下午
    #print('a_startwork------',json.loads(worktime[1].content)['startwork'])
    a_startwork=json.loads(worktime[1].content)['startwork']
    #print('a_startwork_late-------', json.loads(worktime[1].content)['startwork'][0:3]+json.loads(worktime[1].content)['startwork_late']+json.loads(worktime[1].content)['startwork'][5:])
    a_startwork_late=json.loads(worktime[1].content)['startwork'][0:3]+json.loads(worktime[1].content)['startwork_late']+json.loads(worktime[1].content)['startwork'][5:]
    #print('a_endwork------', json.loads(worktime[1].content)['endwork'])
    a_endwork = json.loads(worktime[1].content)['endwork']
    #print('a_endwork_late-------',json.loads(worktime[1].content)['endwork'][0:3] + json.loads(worktime[1].content)['endwork_late'] + json.loads(worktime[1].content)['endwork'][5:])
    if int(json.loads(worktime[1].content)['endwork'][3:5])-int(json.loads(worktime[1].content)['endwork_late'])<0:
        a_endwork_late = str(int(json.loads(worktime[1].content)['endwork'][0:2])-1)+':' + str(60+int(json.loads(worktime[1].content)['endwork'][3:5])-int(json.loads(worktime[1].content)['endwork_late'])) + json.loads(worktime[1].content)['endwork'][5:]
    if int(json.loads(worktime[1].content)['endwork'][3:5]) - int(json.loads(worktime[1].content)['endwork_late']) >= 0:
        a_endwork_late = json.loads(worktime[1].content)['endwork'][0:3] + str(int(json.loads(worktime[1].content)['endwork'][3:5]) - int(json.loads(worktime[1].content)['endwork_late']))  + json.loads(worktime[1].content)['endwork'][5:]

    
    return [m_startwork,m_startwork_late,m_endwork,m_endwork_late,a_startwork,a_startwork_late,a_endwork,a_endwork_late]

# 判断是进还是出
def in_out(direction):
    if direction==0:
        in_out='出'
    if direction==1:
        in_out='进'
    return in_out

#判断上午还是下午
def m_or_a(times):
    if times>=0 and times<=12:
        m_a='上午'
    if times>12 and times<=23:
        m_a='下午'
    return m_a

#判断员工上班的状态(分上午，下午记录)
def get_sys_status(list):
    worktime=str(list[-1])
# 进还是出
    inout=in_out(list[1])
# 上午还是下午
    m_a=m_or_a(int(worktime[8:10]))
# 通行时间
    pass_time=worktime[0:4]+'-'+worktime[4:6]+'-'+worktime[6:8]+' '+worktime[8:10]+':'+worktime[10:12]+':'+worktime[12:14]
    #print(inout,m_a,pass_time)
# 如果为是上午，获取上午的考勤时间
    if m_a=='上午':
        m_startwork=worktime[0:4]+'-'+worktime[4:6]+'-'+worktime[6:8]+' '+definition_time()[0]      #当天上午上班时间（标准）
        m_startwork_late=worktime[0:4]+'-'+worktime[4:6]+'-'+worktime[6:8]+' '+definition_time()[1] # 当天上午迟到时间
        m_endwork=worktime[0:4]+'-'+worktime[4:6]+'-'+worktime[6:8]+' '+definition_time()[2]        #当天上午下班时间
        m_endwork_late=worktime[0:4]+'-'+worktime[4:6]+'-'+worktime[6:8]+' '+definition_time()[3]   # 当天上午早退时间
        m_startwork_late_dt=utc_str_to_timestamp(m_startwork_late)
        m_startwork_dt=utc_str_to_timestamp(m_startwork)
        m_endwork_dt=utc_str_to_timestamp(m_endwork)
        m_endwork_late_dt=utc_str_to_timestamp(m_endwork_late)
        pass_time_dt=utc_str_to_timestamp(pass_time)


        # 如果为进
        if inout=='进':
            if pass_time_dt<=m_startwork_dt:

                status='积极'
            if pass_time_dt >= m_startwork_dt and pass_time_dt<=m_startwork_late_dt:

                status = '正常'
            if pass_time_dt >= m_startwork_late_dt and pass_time_dt<=m_endwork_dt:

                status = '迟到'
        # 如果为出
        if inout=='出':
            if pass_time_dt<=m_endwork_late_dt and pass_time_dt>=m_startwork_late_dt:

                status = '早退'
            else:

                status = '正常'
                # 如果为是上午，获取上午的考勤时间
    if m_a == '下午':
        a_startwork = worktime[0:4] + '-' + worktime[4:6] + '-' + worktime[6:8] + ' ' + definition_time()[
            4]  # 当天下午上班时间（标准）
        a_startwork_late = worktime[0:4] + '-' + worktime[4:6] + '-' + worktime[6:8] + ' ' + \
                           definition_time()[5]  # 当天下午迟到时间
        a_endwork = worktime[0:4] + '-' + worktime[4:6] + '-' + worktime[6:8] + ' ' + definition_time()[
            6]  # 当天下午下班时间
        a_endwork_late = worktime[0:4] + '-' + worktime[4:6] + '-' + worktime[6:8] + ' ' + \
                         definition_time()[7]  # 当天下午早退时间
        a_startwork_late_dt = utc_str_to_timestamp(a_startwork_late)
        a_startwork_dt = utc_str_to_timestamp(a_startwork)
        a_endwork_dt = utc_str_to_timestamp(a_endwork)
        a_endwork_late_dt = utc_str_to_timestamp(a_endwork_late)
        pass_time_dt = utc_str_to_timestamp(pass_time)

        # 如果为进
        if inout == '进':
            if  pass_time_dt <= a_startwork_dt:

                status = '积极'
            if pass_time_dt >= a_startwork_dt and pass_time_dt <= a_startwork_late_dt:

                status = '正常'
            if pass_time_dt >= a_startwork_late_dt and pass_time_dt <=a_endwork_dt:

                status = '迟到'
        # 如果为出
        if inout == '出':
            if pass_time_dt <= a_endwork_late_dt and pass_time_dt >= a_startwork_late_dt:

                status = '早退'
            else:

                status = '正常'
    return (pass_time,status)

#获取该员工每天上午第一条和最后一条记录，下午第一条和最后一条记录,如果抓拍的第一张为进，按照相关参数判断状态是否正常，如第一张为出，说明之前的未能成功抓拍，按正常计算，上午最后一张是否为出，是的话，按照相关参数判断，否则为正常，
#下午最后一张为出，按照相关参数判断是否正常，最后一张为  进  同样为抓拍失败，按正常计算
def get_employee_f_l_list(result):

    # 上午第一张
    if result[0][-1]=='进':
        msg_m_f=[get_name_for_id(result[0][0]),get_status_type(result[0][1]),int(result[0][2][0:4]+result[0][2][5:7]+result[0][2][8:10]),utc_str_to_timestamp(result[0][2])]
    if result[0][-1]=='出':
        msg_m_f= [get_name_for_id(result[0][0]),0,int(result[0][2][0:4] + result[0][2][5:7] + result[0][2][8:10]), utc_str_to_timestamp(result[0][3])]
    # 上午最后一张
    for item in range(len(result)):

        if int(result[item][2][11:13])>int(result[item-1][2][11:13]) and int(result[item][2][11:13])<12:
            if result[0][-1] == '出':
                msg_m_l= [get_name_for_id(result[item][0]), get_status_type(result[item][1]),int(result[item][2][0:4] + result[item][0][2][5:7] + result[item][2][8:10]),utc_str_to_timestamp(result[item][2])]
            if result[0][-1] == '进':
                msg_m_l= [get_name_for_id(result[item][0]), 0,int(result[item][2][0:4] + result[item][2][5:7] + result[item][2][8:10]),utc_str_to_timestamp(result[item][2])]
    # 下午最后一张
    if result[-1][-1]=='出':
        msg_a_f=[get_name_for_id(result[-1][0]),get_status_type(result[-1][1]),int(result[-1][2][0:4]+result[-1][2][5:7]+result[-1][2][8:10]),utc_str_to_timestamp(result[-1][2])]
    if result[-1][-1]=='进':
        msg_a_f=[get_name_for_id(result[-1][0]),0,int(result[-1][2][0:4]+result[-1][2][5:7]+result[-1][2][8:10]),utc_str_to_timestamp(result[-1][2])]

    # 下午第一张
    for item in range(len(result)):
        if int(result[item][2][11:13])>12 :
            if result[0][-1] == '进':
                msg_a_l = [get_name_for_id(result[item][0]), get_status_type(result[item][1]),int(result[item][2][0:4] + result[item][2][5:7] + result[item][2][8:10]),utc_str_to_timestamp(result[item][2])]
            if result[0][-1] == '出':
                msg_a_l = [get_name_for_id(result[item][0]), 0,int(result[item][2][0:4] + result[item][2][5:7] + result[item][2][8:10]),utc_str_to_timestamp(result[item][2])]
            break
    return [msg_m_f,msg_m_l,msg_a_f,msg_a_l]

#从数据库中获取每个员工的通行日志 ( 上午多条记录或者下午多条记录，只取第一次抓拍和最后一次，分上午和下午)  可以通过时间加以筛选
def get_em_log(starttime,endtime):
    starttime=starttime*1000000000
    endtime=endtime*1000000000
    data=FEmployeeLog.select(FEmployeeLog.uid,FEmployeeLog.direction,FEmployeeLog.times).where((FEmployeeLog.times>=int(starttime)) & (FEmployeeLog.times<=int(endtime)))
    result={}
    i=1
    for item in data:
        passtime,status=get_sys_status(list=[item.uid,item.direction,item.times])
        result_list=[get_id_for_name(item.uid),status,passtime,in_out(item.direction)]
        try:
            result[get_id_for_name(item.uid)].append(result_list)
        except:
            result[get_id_for_name(item.uid)]=[]
            result[get_id_for_name(item.uid)].append(result_list)
        print(i)
        i += 1
    for key in result.keys():
        msg=get_employee_f_l_list(result[key])
        for item in msg:
            FDay.insert(uid=item[0],type=item[1],times=item[2],posttime=item[3]).execute()
            break
        break

get_em_log(starttime=20171202,endtime=20171203)


