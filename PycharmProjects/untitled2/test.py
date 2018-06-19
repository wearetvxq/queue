import pymysql




list=[]
max_list=[]
sql_list=[]
two_sta_list=[]
table_list=[]
db= pymysql.connect(host="39.108.165.149",user="wy",password="wy666666",db="xgyd",port=3306,charset='utf8mb4')
cur=db.cursor()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# sql="select * from Xgdl_Basic_Stalist"
# cur.execute(sql)
# result=cur.fetchall()
# print(result[0][1],result[0][2],result[0][3])
# sql_sta="select sta_num from new_test"
# cur.execute(sql_sta)
# result_sta=cur.fetchall()
# for x in range(len(result_sta)):
#     list.append(result_sta[x][0])
# for i in range(len(result)):
#         if result[i][1] not in list:
#                 print(result[i][2]+'_'+result[i][1])
#                 sql1="insert into new_test (`area`,`sta_name`,`ture_pow`,`max_pow`,`is_kt`,`sta_num`,`max_pow(kw.h)`) VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(result[i][3],result[i][2]+'_'+result[i][1],'0.0','0.0','不存在',result[i][1],'0.0')
#                 print(sql1)
#                 cur.execute(sql1)
#                 cur.fetchall()
#                 sql_list.append(sql1)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# sql_find="select xinghao,produce,max_pow from xgyd_gh_kt_sb"
# cur.execute(sql_find)
# result=cur.fetchall()
# for i in range(len(result)):
#         sql_two="update test  set `max_pow`={},`produce`='{}' where `type` = '{}' and sb_type='kt'".format(result[i][2],result[i][1],result[i][0])
#
#         print(sql_two)
#         cur.execute(sql_two)
#         cur.fetchall()
#----------------------------------------------------------------------------------------------------------------
sql1 = "select sta_num from test where sb_type!='kt'"
cur.execute(sql1)
result_num =cur.fetchall()
print('sql2g-----',sql1)
for i in range(len(result_num)):
    if result_num[i][0] not in two_sta_list:
        two_sta_list.append(result_num[i][0])
for x in range(len(two_sta_list)):
    sql_2g_msg="select * from test where sta_num='{}'".format(two_sta_list[x])
    cur.execute(sql_2g_msg)
    msg_list=cur.fetchall()

    max_pow=0
    num_2g = 0
    num_4g = 0
    for y in range(len(msg_list)):
        if msg_list[y][4]=='2G':
            num_2g+=1
            max_pow=max_pow+float(msg_list[y][3])
        if msg_list[y][4]=='4G':
            num_4g+=1
            max_pow=max_pow+float(msg_list[y][3])
    sta_name = msg_list[0][6] + '_' + msg_list[0][1]
    if [msg_list[0][-1],sta_name, max_pow, num_2g, num_4g] not in table_list:
       table_list.append([msg_list[0][-1],sta_name,max_pow,num_2g,num_4g])





for num_list in table_list:

    sql="update jifang_guanli set sta_num ='{}' where sta_name='{}'".format(num_list[1].split('_')[-1],num_list[1])
    print(sql)
    cur.execute(sql)
    cur.fetchall()


db.commit()
cur.close()






