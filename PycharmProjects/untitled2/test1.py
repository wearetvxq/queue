import pymysql




db= pymysql.connect(host="39.108.165.149",user="wy",password="wy666666",db="xgyd",port=3306,charset='utf8mb4')
cur=db.cursor()


sql="select `sta_name`,`city`,`sta_no` from Xgdl_Basic_Stalist where sta_no in (SELECT sta_num from test)"
cur.execute(sql)
reslut=cur.fetchall()
for i in range(len(reslut)):
    sql1="update test set sta_name='{}',area='{}' where sta_num='{}'".format(reslut[i][0],reslut[i][1],reslut[i][2])
    cur.execute(sql1)
    cur.fetchall()
    print(sql1)
db.commit()
cur.close()