#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Auther: ZhengZhong,Jiang

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:python@12.12.11.137:3306/pylearn", max_overflow=5)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class Host(Base):
    __tablename__ = 'host'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    hostname = Column(String(32))
    port = Column(String(32))
    ip = Column(String(32))

    host = relationship('HostUser', secondary=lambda :HostToHostUser.__table__, backref='x')

class HostUser(Base):
    __tablename__ = 'host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)
    username = Column(String(32))


class HostToHostUser(Base):
    __tablename__ = 'host_to_host_user'
    nid = Column(Integer, primary_key=True,autoincrement=True)

    host_id = Column(Integer,ForeignKey('host.nid'))
    host_user_id = Column(Integer,ForeignKey('host_user.nid'))

    host = relationship('Host', backref='h')
    user = relationship('HostUser', backref='u')

# Base.metadata.create_all(engine)

# session.add_all([
#     Host(hostname='c1',port='22',ip='1.1.1.1'),
#     Host(hostname='c2',port='22',ip='1.1.1.2'),
#     Host(hostname='c3',port='22',ip='1.1.1.3'),
#     Host(hostname='c4',port='22',ip='1.1.1.4'),
#     Host(hostname='c5',port='22',ip='1.1.1.5'),
# ])
# session.commit()
#
#
# session.add_all([
#     HostUser(username='root'),
#     HostUser(username='db'),
#     HostUser(username='nb'),
#     HostUser(username='sb'),
# ])
# session.commit()
#
# session.add_all([
#     HostToHostUser(host_id=1,host_user_id=1),
#     HostToHostUser(host_id=1,host_user_id=2),
#     HostToHostUser(host_id=1,host_user_id=3),
#     HostToHostUser(host_id=2,host_user_id=2),
#     HostToHostUser(host_id=2,host_user_id=4),
#     HostToHostUser(host_id=2,host_user_id=3),
# ])
# session.commit()

# host_obj = session.query(Host).filter(Host.hostname == 'c1').first()
# host_to_hostuser = session.query(HostToHostUser.host_user_id).filter(HostToHostUser.host_id == host_obj.nid).all()
#
# r = zip(*host_to_hostuser)
#
# ret = session.query(HostUser.username).filter(HostUser.nid.in_(list(r)[0])).all()
# print(ret)

ret = session.query(Host).filter(Host.hostname=='c1').first()

# 方式一
# for item in ret.h:
#     print(item.user.username)

# 方式二

print(ret.host)