def pro():
    s=input("enter the text :").split()
    n=0
    for i in s:
        n+=1
    print(n)
pro()
p=input("wanna try agin : ")
while p =="yes":
    pro()
    p=input("wanna try agin : ")