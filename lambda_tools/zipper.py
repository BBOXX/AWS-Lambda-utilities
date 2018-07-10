from glob import glob
import os
import zipfile

# Path to the site-packages directory, for example ../dp-env/lib/python3.6/site-packages/
PATH_TO_VIRTUAL_ENV_PACKAGES = '../example-env/lib/python3.6/site-packages/'

# Where the script will go to look for files to add to the zip package to add to the root of zip
LOOKUP_PATHS = ['../*.py', '../*.ini']

# Files included in the list above but that you do not wish to send to lambda such as unit tests
FILES_TO_EXCLUDE = ['../unit_tests.py']

# Destination path where the zip folder should be created
ZIP_PATH = './lambda_function.zip'


def addFilesFromLookUpPaths(zipf):
    """
    Looks for the files that correspond the format specified in the LOOKUP_PATHS list
    and adds them to the root of the zip file
    """
    filesToAdd = [filePath for lookupPath in LOOKUP_PATHS
                  for filePath in glob(os.path.join(lookupPath))
                  if filePath not in FILES_TO_EXCLUDE]
    for fileToAdd in filesToAdd:
        # set destination path to root of zip file by removing extra dot
        destinationPath = os.path.join(fileToAdd[1:])
        zipf.write(fileToAdd, destinationPath)
    print('Added {} files found from the look up paths list to the zip package'.format(
        len(filesToAdd)))


def addLibrariesToZip(zipf):
    """
    Adds all packages in the PATH_TO_VIRTUAL_ENV_PACKAGES to the zip file
    """
    for packageToAdd in glob(os.path.join(PATH_TO_VIRTUAL_ENV_PACKAGES, '**/*'), recursive=True):
        # removes excess subdirectories as required by aws
        destinationPath = os.path.join(*packageToAdd.split('/')[5:])
        zipf.write(packageToAdd, destinationPath)
    print('Added the packages files from the virtual env path: {}'.format(
        PATH_TO_VIRTUAL_ENV_PACKAGES))


if __name__ == '__main__':
    zipf = zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED)
    addFilesFromLookUpPaths(zipf)
    addLibrariesToZip(zipf)
    zipf.close()
