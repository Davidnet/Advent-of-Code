import hashlib

strings = "yzbqklnj"
candidates = list(range(10, 100000000))

for i in candidates:
    candidate = strings + str(i)
    # print(candidate)
    candidate = candidate.encode('utf-8')
    candidate = hashlib.md5(candidate).hexdigest()
    # print("The hex is\n " + candidate + '\n')
    if len(candidate) > 6:
        if candidate[:6] == '000000':
            print("Solution encounter \n" + "with i " + str(i))
            print("\n" + candidate)
            break
print("End Of Program")
