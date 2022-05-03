#!/usr/bin/env python3

import os
import sys
import time
import subprocess
from asyncio.subprocess import DEVNULL
from PIL import Image

def upload(images):
    for image in images:
        createdate = time.localtime(os.stat(image).st_birthtime)
        year = createdate.tm_year
        month = createdate.tm_mon
        dstpath = f"/Users/waderwu/blog-img/{year}/{month}"
        if not os.path.isdir(dstpath):
            os.makedirs(dstpath)
        imgname = os.path.basename(image)
        if os.path.isfile(image):
            webp = f"{dstpath}/{imgname}.webp"
            Image.open(image).convert("RGB").save(webp, "webp")
            imgname = os.path.basename(image)
            imgurl = f"https://raw.githubusercontent.com/waderwu/blog-img/master/{year}/{month}/{imgname}.webp"
            print(imgurl)
        
    subprocess.check_output(["bash", "-c", f"cd /Users/waderwu/blog-img/; git pull ; git add . ; git commit -m 'add {year}-{month}' ; git push"], stderr=DEVNULL)


if __name__ == "__main__":
    images = sys.argv[1:]
    upload(images)