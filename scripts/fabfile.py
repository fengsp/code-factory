# -*- coding: utf-8 -*-
from fabric.api import *


env.user = 'root'
env.hosts = ['192.168.4.167']


def test():
    local("python test.py")


def pack():
    local("tar zcf /tmp/project.tar.gz ./project")


def upload():
    put('/tmp/project.tar.gz', '/tmp/project.tar.gz')


def fire():
    with cd('/tmp'):
        run('tar zxf /tmp/project.tar.gz')
    with cd('/tmp/project'):
        run('python app.py')


def deploy():
    test()
    pack()
    upload()
    fire()
