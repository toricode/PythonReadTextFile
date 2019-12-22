f = open('test_unicode.txt', 'r', encoding='utf-8')

for line in f:
    print(line)

f.close()