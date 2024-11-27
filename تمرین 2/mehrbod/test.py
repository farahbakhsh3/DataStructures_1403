from main import toPostfix, toPrefix

if __name__ == "__main__":
    print(toPostfix("a+b*c"))   # abc*+
    print(toPrefix("a+b*c"))    # +a*bc

    print(toPostfix("a/b+c/d")) # ab/cd/+
    print(toPrefix("a/b+c/d"))  # +/ab/cd