#!/usr/bin/env python
# -*- coding:utf-8 -*-
from sqlalchemy import create_engine,and_,or_,func,Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,ForeignKey,UniqueConstraint,DateTime
from  sqlalchemy.orm import sessionmaker,relationship

Base = declarative_base() #生成一个SqlORM 基类

# 程序登陆用户和服务器账户，一个人可以有多个服务器账号，一个服务器账号可以给多个人用
UserProfile2HostUser= Table('userprofile_2_hostuser',Base.metadata,
    Column('userprofile_id',ForeignKey('user_profile.id'),primary_key=True),
    Column('hostuser_id',ForeignKey('host_user.id'),primary_key=True),
)


class Host(Base):
    __tablename__='host'
    id = Column(Integer,primary_key=True,autoincrement=True)
    hostname = Column(String(64),unique=True,nullable=False)
    ip_addr = Column(String(128),unique=True,nullable=False)
    port = Column(Integer,default=22)

	
class HostUser(Base):
    __tablename__ = 'host_user'
    id = Column(Integer,primary_key=True)
    AuthTypes = [
        (u'ssh-passwd',u'SSH/Password'),
        (u'ssh-key',u'SSH/KEY'),
    ]
    auth_type = Column(String(64))
    username = Column(String(64),unique=True,nullable=False)
    password = Column(String(255))

    host_id = Column(Integer,ForeignKey('host.id'))
	
	host = relationship('Host',backref='uu')
    
    __table_args__ = (UniqueConstraint('host_id','username', name='_host_username_uc'),)


		
#  
# obj = session.query(HostUser.username,HostUser.password,Host.hostname,Host.port).join(Host).filter(HostUser.id == 1).first()
# (用户名，密码，主机名，端口)

class UserProfile(Base):
    __tablename__ = 'user_profile'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True,nullable=False)
    password = Column(String(255),nullable=False)
	# 如果是一个人只能在一个组下
	group_id = Column(Integer,ForeignKey('group.id'))
	
    host_list = relationship('HostUser',secondary=UserProfile2HostUser,backref='userprofiles')

"""
# 输入用户名和密码：
# 
obj = session.query(UserProfile).filter(username=输入的用户名, password=输入的密码).first()
if not obj:
	# 堡垒机登录用户对象
	# 输入这个人的所有机器
	obj.host_list # 当前堡垒机登录用户，所有的服务器用户名
	# 
	for item  in obj.host_list:
		# item,是一个HostUser对象
		item.password,item.username, 
		# item.host 对象，host对象
		item.host.hostname,item.host.port
	# item 目标机器HostUser对象
	host_obj = input(:...)
	session.add(AuditLog(userprofile_id=obj.id,hostuser_id = host_obj.id, "ifconfig"))
"""

class AuditLog(Base):
    __tablename__ = 'audit_log'
    id = Column(Integer,primary_key=True)
    userprofile_id = Column(Integer,ForeignKey('user_profile.id'))
    hostuser_id = Column(Integer,ForeignKey('host_user.id'))

    cmd = Column(String(255))
    date = Column(DateTime)
	

"""
class Session:
	session = None
	def __init__():
		engine = create_engine("mysql+pymysql://root:123@127.0.0.1:3306/s13", max_overflow=5)
		ss = sessionmaker(bind=engine)
		obj = ss()
		Session.session = obj
		
	@classmethod	
	def instance(cls):
		if not cls.session:
			cls()
		return cls.session
"""





