t=int(input("enter number of strings to check"))
for t in range(0,t):
    p=input("enter dictionary")
    s=input("enter lexical keyword")

    sorted=''
    for search in p:
        if search in s:
            # print("".join(search),end="")
            sorted+=(search)
    print(sorted)