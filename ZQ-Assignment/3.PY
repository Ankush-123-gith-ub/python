# 3: Wonderful Chocolate Offer 
# Scenario: You have an uncle who daily gives you D chocolates up to N days. Also, you have C 
# chocolates already but your parents allow you only to eat one chocolate per day. Calculate the total 
# chocolates at the end of N days.
# Sample Input 0
# 5 5 5
# Sample Output 0
# 25

d = int(input())
n = int(input())
c = int(input())
a = (d*n+c)-n
print(a)