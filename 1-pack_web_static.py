#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive from the contents of the
web_static folder of your AirBnB Clone repo, using the function do_pack."""

from datetime import datetime
from fabric.api import local


def do_pack():
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    fname = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/{} web_static".format(fname))
    if archive.failed:
        return None
    return "versions/{}".format(fname)
