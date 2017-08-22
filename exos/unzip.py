import os
import tarfile
import zipfile
import shutil
def dezip(archive) :
	if (zipfile.is_zipfile(archive)):
		directory = os.path.splitext(archive)[0]
		with zipfile.ZipFile(archive, "r") as z:
			if (os.path.isdir(directory)):
				shutil.rmtree(directory)
			z.extractall(directory)
			listdir = os.listdir(directory)
			if (len(listdir) == 1):
				shutil.move(os.path.join(directory,listdir[0]), 'temp')
				os.rmdir(directory)
				shutil.move('temp', directory)
	elif (archive.endswith("tar.gz")):
		directory = os.path.splitext(archive)[0][:-4]
		tar = tarfile.open(archive, "r:gz")
		tar.extractall()
		tar.close()
	elif (archive.endswith("tar")):
		directory = os.path.splitext(archive)[0]
		tar = tarfile.open(archive, "r:")
		tar.extractall()
		tar.close()  

	os.remove(archive)
	return directory