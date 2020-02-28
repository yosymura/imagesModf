import os
import shutil

from_dir = "D://--mentes--"
to_dir = "D://Mentes/audiok"

pic_ext = ['.PNG','.JPEG','.JPG','.BMP','.DDS','.GIF','.HEIC','.PSD','.PSPIMAGE','.TGA','.THM','.TIF','.TIFF','.YUV']
audio_ext = ['.MP3','.AAC','.WAV','.FLAC','.ALAC','.DSD','.AIF','.IFF','.M3U','.M4A','.MID','.MPA','.WMA']
video_ext = ['.MKV','.MP4','.AVI','.WMV','.MOV','.FLV','.AVCHD','.3G2','.3GP','.ASF','.M4V','.MPG','.RM','.SRT','.SWF','.VOB','.WMV']
text_ext = ['.TXT','.DOC','.DOCX','.LOG','.MSG','.ODT','.PAGES','.RTF','.TEX','.WPD','.WPS]']
data_ext = ['.CSV','.GED','.KEYCHAIN','.PPS','.PPT','.PPTX','.SDF','.TAR','.VCF','.XML']
pageLayout_ext = ['.INDD','.PCT','.PDF']
spreadsheet_ext = ['.XLR','.XLS','.XLSX']
database_ext = ['.ACCDB','.DB','.DBF','.MDB','.PDB','.SQL']
xecutable_ext = ['.APK','.APP','.CGI','.GADGET','.JAR']
cad_ext = ['.DWG','.DXF']
web_ext = ['.ASP','.ASPX','.CER','.CFM','.CSR','.CSS','.DCR','.HTM','.HTML','.JS','.JSP','.PHP','.RSS','.XHTML']
compressed_ext = ['.7Z','.CBR','.GZ','.RAR','.TAR.GZ','.ZIP','.ZIPX']
diskImage_ext = ['.BIN','.CUE','.ISO','.MDF','.TOAST','.VCD']
developer_ext = ['.C','.CLASS','.CPP','.CS','.DTD','.FLA','.H','.JAVA','.LUA','.M','.PL','.PY','.SH','.SLN','.SWIFT','.VB','.VCXPROJ','.XCODEPROJ']



def copyFunc(ext,src,dist):
	for root, dirs, files in os.walk(src):
		for file in files:
			if file.endswith(tuple(ext)):
				file_url = os.path.join(root, file)
				shutil.copy2(file_url, dist)
	print("Copy finished!")

copyFunc(audio_ext,from_dir,to_dir)