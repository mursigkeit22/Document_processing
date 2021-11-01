import glob
import os

# files and folders
root_dir = r"C:\mein\some_things\тексты\NewMicrosoftWordDocument2"
for filename in glob.iglob(root_dir + '**/**', recursive=True):
    print(filename)

print("_____________________")
# only files
for filename in glob.iglob(root_dir + '**/**', recursive=True):
    if os.path.isfile(filename):
        print(filename)
