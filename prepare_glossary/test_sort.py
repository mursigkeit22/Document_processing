test_list = ["Abra", "abra", "Bot", "bot", "something", "Something", "abba", "", "", "", "", ]
test_list.sort()
print(test_list)

test_list = ["Abra", "abra", "Bot", "bot", "something", "Something", "abba", "", "", "", "", ]
test_list.sort(key=lambda x: x.casefold())
print(test_list)
