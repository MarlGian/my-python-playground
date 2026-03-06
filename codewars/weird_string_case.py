def to_weird_case(words):
    word = words.split()
    obj = []
    for i in range(len(word)):
        temp = word[i] + " "
        for j in range(len(temp)):
            if j % 2 == 0:
                obj += temp[j].upper()
            else:
                obj += temp[j].lower()
    return "".join(obj[0:-1:])
