import os
import shutil
from typing import Union

from_dir = "D:\\..."
to_dir = "D:\\..."

pic_ext = ['.PNG','.JPEG','.JPG']
audio_ext = ['.MP3','.AAC','.WAV','.FLAC','.ALAC','.DSD']
video_ext = ['.MKV','.MP4','.AVI','.WMV','.MOV','.FLV','.AVCHD']


def copyFunc(ext,src,dist):
		for root, dirs, files in os.walk(src):
			for file in files:
				if file.endswith(tuple(ext)):
					file_url = os.path.join(root, file)
					shutil.copy2(file_url, dist)
		print("Copy finished!")

copyFunc(pic_ext,from_dir,to_dir)