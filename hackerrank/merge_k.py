import textwrap
def merge_the_tools(string, k):
    l= textwrap.wrap(string,k)
    for i in l:
        print("".join((set(i))))
    
