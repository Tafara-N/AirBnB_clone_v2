#!/usr/bin/python3

"""
Generating a '.tgz' archive from the contents of the web_static folder
"""

import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Creating a 'tar gzipped' archive of the web_static directory
    """

    date_time = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        date_time.year,
        date_time.month,
        date_time.day,
        date_time.hour,
        date_time.minute,
        date_time.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
