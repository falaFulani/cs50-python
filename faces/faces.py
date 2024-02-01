def main ():
    c = input()
    c = convert(c)
    print(c)
def convert(c):
    c = c.replace(":)","🙂")
    c = c.replace(":(" , "🙁")
    return c

main()
