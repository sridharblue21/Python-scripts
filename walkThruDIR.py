import os

for folders,subFolders, filenames in os.walk('D:\SRI\pyScripts'):
    print('folders are: ' + folders)
    print('subfolders are: ' + str(subFolders))
    print('filenames are: ' + str(filenames))
    print()
