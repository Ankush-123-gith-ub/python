# Sample Input 0
# 80&69&65&75&85
# Sample Output 0
# PEAKU
n =input("")
list = []
for i in n:
    a=n.split("&")
for j in a:
    b = chr(int(j))
    list.append(b)
word = "".join(list)
print(word)