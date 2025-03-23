def main():
    try:
        a=int(input("Hey,Enter a number: "))
        print(a)
        return

    except Exception as E:
        print(E)
        return

    finally:
        print("I am inside finally.")
main()