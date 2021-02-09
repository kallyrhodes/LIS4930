def insert_sting_middle(str, word):
    length=len(str)//2
    s=str[:length] + word + str[length:]
    return s
print(insert_sting_middle('[[]]', 'Python'))
