from peewee import *

database = MySQLDatabase('face', **{'host': '39.108.165.149', 'port': 3306, 'user': 'root','password':'lcj123456'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class FSysAttendance(BaseModel):
    content = TextField()
    type = IntegerField()

    class Meta:
        db_table = 'f_sys_attendance'

class FSysEmployee(BaseModel):
    id=IntegerField()
    desc = CharField()
    pic = CharField()
    posttime = IntegerField()
    sex = IntegerField()
    status = IntegerField()
    tment = IntegerField()
    username = CharField()

    class Meta:
        db_table = 'f_sys_employee'

class FSysRouter(BaseModel):
    desc = TextField(null=True)
    level = IntegerField()
    name = CharField()
    path = CharField()
    status = IntegerField()
    template = CharField(null=True)
    type = IntegerField()
    pid = IntegerField()

    class Meta:
        db_table = 'f_sys_router'

class FSysRule(BaseModel):
    code = IntegerField()
    router = TextField()

    class Meta:
        db_table = 'f_sys_rule'

class FSysTment(BaseModel):
    id=IntegerField()
    name = CharField()
    posttime = IntegerField()
    status = IntegerField()
    total = IntegerField()
    desc = CharField()

    class Meta:
        db_table = 'f_sys_tment'

class FSysUser(BaseModel):
    id = IntegerField()
    mail = CharField()
    passwd = CharField()
    posttime = IntegerField()
    status = IntegerField()
    tment = IntegerField()
    username = CharField()

    class Meta:
        db_table = 'f_sys_user'

class FVisitorsLog(BaseModel):
    id=IntegerField()
    end = IntegerField()
    interviewed = CharField()
    pic = TextField(null=True)
    starttime = IntegerField()
    status = IntegerField()
    team = IntegerField()
    total = IntegerField()
    username = CharField()
    visitid = CharField(db_column='visitId')
    purpose = CharField()
    phone = CharField()
    #desc=CharField()

    class Meta:
        db_table = 'f_visitors_log'

class FPurpose(BaseModel):
    name = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'f_purpose'

class FMonth(BaseModel):
    id= IntegerField()
    uid = IntegerField()
    tid = IntegerField()
    username = CharField()
    normal = IntegerField()
    late = IntegerField()
    off = IntegerField()
    early = IntegerField()
    absence = IntegerField()
    posttime = IntegerField()

    class Meta:
        db_table = 'f_month'

class FDay(BaseModel):
    uid = IntegerField()
    type = IntegerField()
    times = IntegerField()
    posttime = IntegerField()

    class Meta:
        db_table = 'f_day'


class FLog(BaseModel):
    id=IntegerField()
    type = IntegerField()
    status = IntegerField()
    content = TextField()
    posttime = IntegerField()
    pic = TextField()

    class Meta:
        db_table = 'f_log'


class FFeature(BaseModel):
    uid = IntegerField()
    feature = TextField()

    class Meta:
        db_table = 'f_feature'


class FEmployeeLog(BaseModel):
    uid = IntegerField()
    camid = CharField()
    direction = IntegerField()
    times = IntegerField()
    pic = CharField()
    posttime = IntegerField()


    class Meta:
        db_table = 'f_employee_log'
