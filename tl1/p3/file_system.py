import os

def list_files(path):
	try:
		return os.listdir(path)
	except Exception as e:
		print('ERROR!!! ', e)
		return None
