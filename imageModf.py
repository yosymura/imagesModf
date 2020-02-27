import os
import shutil

from_dir = "D:\\..."
to_dir = "D:\\..."

pic_ext=['.png','.jpeg','.jpg']
audio_ext=[]
video_ext= []


def copyFunc(ext,src,dist):
		for root, dirs, files in os.walk(src):
			for file in files:
				if file.endswith(tuple(ext)):
					file_url = os.path.join (root, file)
					shutil.copy2(file_url, dist)
		print("Copy finished!")

copyFunc(pic_ext,from_dir,to_dir)