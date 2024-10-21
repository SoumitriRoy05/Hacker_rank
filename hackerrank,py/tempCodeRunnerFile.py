n=int(input("Enter a number:"))
if n%2!=0:
    print("WEIRD")
elif n%2==0 & 2<n<5:
    print("NOT WEIRD")
elif n%2==0 & 6<n<20:
    print("WEIRD")
elif n%2==0 & n<20:
    print("NOT WEIRD")
else:
    print("NULL")