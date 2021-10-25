with open("work_docs/TASS_done.txt", "w", encoding="utf8") as done_file:
    done_file.write("")
def isEnglish(s):
    if "’" in s:
        s = s.replace("’", "'")
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        if "Acrobat Reader" not in s:
            with open("work_docs/TASS_done.txt", "a", encoding="utf8") as done_file:
                done_file.write(s)

        print("FALSE ", s)
        return False
    else:
        print("TRUE ", s)
        return True


with open("work_docs/TASS.txt", "r", encoding="utf8") as f:
    lines = f.readlines()

for line in lines:
    isEnglish(line)