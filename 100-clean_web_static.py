#!/usr/bin/python3
""" Write a Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the function do_deploy """

from fabric.api import *
from datetime import datetime
from os.path import isfile, splitext, basename

# Servers
env.hosts = [
    '35.231.119.161',
    '54.157.250.190'
]
# Username
env.user = 'ubuntu'
env.key_filename = "~/.ssh/holberton"


def do_pack():
    """ Pack web_static into a tarball """
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    fname = "web_static_" + time + ".tgz"
    local("mkdir -p versions")
    archive = local("tar -cvzf versions/{} web_static".format(fname))
    if archive.failed:
        return None
    return "versions/{}".format(fname)


def do_deploy(archive_path):
    """ Deploy a tarball to web_server(s) """
    # Returns False if the file at the path archive_path doesn't exist
    if not isfile(archive_path):
        return False
    # Uploads archive to the /tmp directory of the web server
    put(archive_path, '/tmp')

    # Archive_name without the .tgz extension or the parent directories
    archive_name = splitext(basename(archive_path))[0]

    print("shit")
    # Create the directory (if not exists) that the files will be moved to
    run("mkdir -p /data/web_static/releases/{}".format(archive_name))

    # Decompress the archive to the folder
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
        .format(archive_name, archive_name))

    # Delete the archive (tarball) from the web server
    run("rm /tmp/{}.tgz".format(archive_name))

    # Delete the symbolic link from the web server
    run("rm -rf /data/web_static/current")

    # Create a new symbolic link, linked to the newest version
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(archive_name))

    # Remove redundant directory
    run("mv /data/web_static/current/web_static/* /data/web_static/current/")
    run("rm -rf /data/web_static/current/web_static")

    # Deployed
    print("New version deployed!")
    return True


def deploy():
    """ Create and distribute an archive to your web servers """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """ Clean up old archives """
    number = 2 if int(number) < 2 else int(number) + 1
    local("ls -1t versions/ | tail -n +{} | xargs rm"
          .format(number))
    run("ls -1t /data/web_static/releases | tail -n +{} | xargs rm"
        .format(number))
