#!/usr/bin/env python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    # Create the 'versions' folder if it doesn't exist
    if not os.path.exists('versions'):
        os.makedirs('versions')

    # Create the name of the archive file
    now = datetime.now()
    archive_name = 'versions/web_static_{}{}{}{}{}{}.tgz'.format(
        now.year, now.month, now.day, now.hour, now.minute, now.second)

    # Compress the web_static folder into the archive
    result = local("tar -cvzf {} web_static".format(archive_name))

    # Check if the compression was successful
    if result.failed:
        return None
    else:
        return archive_name
