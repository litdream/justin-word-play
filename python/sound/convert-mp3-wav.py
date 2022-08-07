import os
import sys
import platform
import glob
import subprocess
import logging
logging.basicConfig(level=logging.DEBUG)

cmd = "where" if platform.system() == "Windows" else "which"
cmdcli = f'{cmd} ffmpeg'
logging.debug(cmdcli)
rtn = subprocess.getstatusoutput(cmdcli)
if rtn[0] != 0:
    logging.critical("ffmpeg not found.  Please install 'ffmpeg'")
    sys.exit(1)
ffmpeg = rtn[1]
logging.debug(ffmpeg)

for f in glob.glob("*.mp3"):
    wav = f.replace(".mp3", ".wav")
    if not os.path.exists(wav):
        os.system(f"{ffmpeg} -i {f} {wav}")
    else:
        logging.info("{wav} exists.  Skipping.")
