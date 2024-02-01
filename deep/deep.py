def check():
    n = input("What is the Answer to the Great Question of Life, the Universe, and Everything?: ")
    n = n.strip().lower()
    if n == "42":
        print ("Yes")
    elif n == "forty two":
        print("Yes")
    elif n == "forty-two":
        print ("Yes")
    else:
        print("No")

check()
