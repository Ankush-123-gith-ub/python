def generate_table(n):
    with open (f"tables/table{n}.txt","w") as t:
        for i in range(1,11):
            a=(f"{n} x {i} = {n*i}\n")
            t.write(a)
for j in range(2,21):
    generate_table(j)




