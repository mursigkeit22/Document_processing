import random


def count_numbers(value):
    count = 0
    for character in value:
        if character.isdigit():
            count += 1
    return count


def is_english(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True


with open(r'C:\Users\Valeria.Shelgunova\Downloads\рандомизатор\src.txt', "r", encoding="utf-8") as f:
    lines = f.readlines()
    # for line in enumerate(lines[:20], start=1):
    #     print(line)
print(len(lines))
with open(r'new.txt', "w", encoding="utf-8") as new_ff:
    pass

number_list = []
with open(r'new.txt', "a", encoding="utf-8") as new_f:
    for number, line in enumerate(lines, start=1):
        split_line = line.split()
        if len(split_line) > 5:
            if not is_english(line):
                continue
            if " " in line \
                    or "+" in line \
                    or "■" in line or "~" in line or "<" in line or "[" in line or "]" in line:
                continue
            count = count_numbers(line)
            if count < 5:
                number_list.append(number)
                new_f.write(line)


print(number_list)
print(len(number_list))
with open(r'new.txt', "r", encoding="utf-8") as new_f:
    lines = new_f.readlines()
    print(len(lines))


# shuffled_list = random.sample(number_list, 750)
# print(len(shuffled_list))
# print(shuffled_list)
#                    # or "/" in line \

