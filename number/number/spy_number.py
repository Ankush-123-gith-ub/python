n = int(input("Enter: "))
p_o_d = 1
s_o_d = 0
while n != 0:
    a = n % 10
    s_o_d = s_o_d + a
    p_o_d = p_o_d * a
    n = n // 10
print(s_o_d)
print(p_o_d)
if s_o_d  == p_o_d:
    print("Spy Number.")
else:
    print("Not Spy Number.")


