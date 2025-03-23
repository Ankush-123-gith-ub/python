# 4: Ant Consensus
# Scenario: There is a group of ants that on the start of the day makes itself K times, it was the previous 
# day. Initially, its count was C. You have to find its population on N th day.
# Sample Input 0
# 4 9 3
# Sample Output 0
# 2916

c = int(input())
k = int(input())
n = int(input())
a = c*(k)**n
print(a)

