from os import listdir
from os.path import isfile, join
import re

mypath = "./templates"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]


for file_name in onlyfiles:
    with open(f"./templates/{file_name}", 'r') as f:
        contents = f.read()
        pattern = "(<MinimumMatchValue>)(.*)(</MinimumMatchValue>)"
        # check if it is the only find
        found = re.findall(pattern, contents)
        if len(found) > 1:
            print(f"File {file_name} has more than one occurence of pattern {pattern}.")
            break

        temp_contents = re.sub(pattern, "<MinimumMatchValue>75</MinimumMatchValue>", contents)
        with open(f"./new_templates/{file_name}", "w") as new_f:
            new_f.write(temp_contents)
