# Author:Alex Li
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,Table
from sqlalchemy.orm import sessionmaker, relationship
engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s13", max_overflow=5)

Base = declarative_base()
# 单表
class Test(Base):
    __tablename__ = 'test'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    name = Column(String(32))
# 一对多
class Group(Base):
    __tablename__ = 'group'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    caption = Column(String(32))

class User(Base):
    __tablename__ = 'user'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))
    group_id = Column(Integer, ForeignKey('group.nid'))
    group = relationship("Group", backref='uuu')

    def __repr__(self):
        temp = "%s - %s: %s" %(self.nid, self.username, self.group_id)
        return temp


# print(type(HostToHostUser.__table__))

# HostToHostUser = Table('host_to_host_user',Base.metadata,
#     Column('host_id',ForeignKey('host.nid'),primary_key=True),
#     Column('host_user_id',ForeignKey('host_user.nid'),primary_key=True),
# )

class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)

    host_id = Column(Integer ,ForeignKey('host.nid'))
    host_user_id = Column(Integer, ForeignKey('host_user.nid'))

class Host(Base): # metaclass,Host.table对象
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))

    # host_user = relationship('HostUser', secondary=HostToHostUser, backref='h')
    host_user = relationship('HostUser', secondary=HostToHostUser.__table__, backref='h')

class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))



    # host = relationship("Host", backref='h')
    # host_user = relationship("HostUser", backref='u')


# def init_db():
#     Base.metadata.create_all(engine)
#
# def drop_db():
#     Base.metadata.drop_all(engine)

# init_db()
# Session = sessionmaker(bind=engine)
# session = Session()

# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()


# session.add_all([
#     HostUser(username='root'),
#     HostUser(username='db'),
#     HostUser(username='nb'),
#     HostUser(username='sb'),
# ])
# session.commit()

# session.add_all([
#     HostToHostUser(host_id=1,host_user_id=1),
#     HostToHostUser(host_id=1,host_user_id=2),
#     HostToHostUser(host_id=1,host_user_id=3),
#     HostToHostUser(host_id=2,host_user_id=2),
#     HostToHostUser(host_id=2,host_user_id=4),
#     HostToHostUser(host_id=2,host_user_id=3),
# ])
# session.commit()


# session.add(Group(caption='dba'))
# session.add(Group(caption='ddd'))
# session.commit()

# session.add_all([
#     User(username='alex1',group_id=1),
#     User(username='alex2',group_id=2)
# ])
# session.commit()

# 只是获取用户
# ret = session.query(User).filter(User.username == 'alex1').all()
# print(ret)
# ret = session.query(User).all()
# obj = ret[0]
# print(ret)
# print(obj)
# print(obj.nid)
# print(obj.username)
# print(obj.group_id)

# ret = session.query(User.username).all()
# print(ret)
# sql = session.query(User,Group).join(Group, isouter=True)
# print(sql)
# ret = session.query(User,Group).join(Group, isouter=True).all()
# print(ret)
# sql = session.query(User.username,Group.caption).join(Group, isouter=True)
# print(sql)
# ret = session.query(User.username,Group.caption).join(Group, isouter=True).all()
# print(ret)
# select * from user left join group on user.group_id = group.nid

# 原始方式
# ret = session.query(User.username,Group.caption).join(Group, isouter=True).all()
# 新方式（正向查询）
# ret = session.query(User).all()
# for obj in ret:
#     # obj代指user表的没一行数据
#     # obj.group代指group对象，
#     print(obj.nid,obj.username,obj.group_id, obj.group,obj.group.nid,obj.group.caption)

# 原始方式
# ret = session.query(User.username,Group.caption).join(Group, isouter=True).filter(Group.caption == 'DBA').all()
# 新方式（反向查询）
# obj = session.query(Group).filter(Group.caption == 'DBA').first()
# print(obj.nid)
# print(obj.caption)
# print(obj.uuu)

# sql = session.query(Group).filter(Group.caption == 'DBA')
# print(sql)

# sql = session.query(Group).get(1)
# print(sql)



# ==== 多对多


# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()


# session.add_all([
#     HostUser(username='root'),
#     HostUser(username='db'),
#     HostUser(username='nb'),
#     HostUser(username='sb'),
# ])
# session.commit()

# session.add_all([
#     HostToHostUser(host_id=1,host_user_id=1),
#     HostToHostUser(host_id=1,host_user_id=2),
#     HostToHostUser(host_id=1,host_user_id=3),
#     HostToHostUser(host_id=2,host_user_id=2),
#     HostToHostUser(host_id=2,host_user_id=4),
#     HostToHostUser(host_id=2,host_user_id=3),
# ])
# session.commit()

# 需求来了。。。
# 获取主机1中所有用户

"""
# 1
host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# host_obj.nid
session.query()
session.query(Host.nid).filter(Host.hostname == 'c1')

# 2,所有用户ID
host_2_host_user = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()

# print(host_2_host_user)
# [(1,), (2,), (3,)]
r = zip(*host_2_host_user)
# print(list(r)[0])
# [1,2,3]
# 3、根据用户ID找到所有用户
users = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
print(users)
"""

# 原始方式
# session.query(HostUser.name).filter(HostUser.nid.in_(session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == session.query(Host.nid).filter(Host.hostname == 'c1'))))

"""
host_obj = session.query(Host).filter(Host.hostname=='c1').first()
print(host_obj.nid)
print(host_obj.hostname)
# 第三表对应的对象
print(host_obj.h)
# 循环获取的第三表对应的对象
for item in host_obj.h:
    print(item.host_user,item.host_user.nid,item.host_user.username)
"""
# host_obj = session.query(Host).filter(Host.hostname=='c1').first()
# for item in host_obj.h:
#     print(item.host_user.username)

host_obj = session.query(Host).filter(Host.hostname == 'c1').first()


print(host_obj.host_user)
for item in host_obj.host_user.xxxx:
    print(item.username)


