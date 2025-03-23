# s =input()
# s_len = len(s)
# count_a = 0
# for i in s:
#     if i.isalnum():
#         count_a += 1
# print(f"Length of character {s_len - count_a}")

def count(s):
    count_c = 0
    for i in s:
        if not i.isalnum():
            count_c += 1
    return f"Length of character {count_c}"
print(count("bdbkdsfhb332()"))