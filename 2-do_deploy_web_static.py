#!/usr/bin/python3

"""
Distrubiting archives on the web servers based on the
`1-pack_web_static.py` file
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['100.26.159.205', '54.237.14.183']


def do_deploy(archive_path):
    """
    Distributing the archive to the web servers

    Servers:
        web-01: 100.26.159.205
        web-02: 54.237.14.183
    """

    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, no_ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
        run('rm /tmp/{}'.format(file_name))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
        run('rm -rf {}{}/web_static'.format(path, no_ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except:
        return False