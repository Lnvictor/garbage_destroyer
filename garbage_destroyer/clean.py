import glob
import os
from datetime import datetime


def clean(time_diff, ext, dir):
    path = f"{dir}/*"

    if ext:
        path += f'.{ext}'

    for item in glob.glob(path):
        last_access = datetime.fromtimestamp(os.path.getatime(item))
        delta = datetime.now() - last_access
        
        if os.path.isfile(item) and delta.days > time_diff:
            os.remove(item)