#!/usr/bin/python3

"""
Deleting all out of date archives

execute:
fab -f 100-clean_web_static.py do_clean:number=2 \
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['100.26.159.205', '54.237.14.183']


def do_clean(number=0):
    """
    Deleting all out of date archives

    Args:
        number (int): Number of archives to be kept

    If number is 0 or 1, only the most recent archive will be kept.
    If number is 2, the most and second-most recent archives are kept,
    etc.
    """

    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for _ in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for arch in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [arch for arch in archives if "web_static_" in arch]
        [archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(a)) for arch in archives]
