name = input("Enter your name ")
print("Welcome", name)

answer = input("Aap ko rashan laane ko bheja gaya h lekin aap ek saman gira aate h ab aap wapas jaane k liye left loge ya right?")

if answer == "left":
    print("yaha toh aap aaye hi nahi the boss")

elif answer == "right":
    print("Aap doodh k packet k liye road cross ki thi? (yes/no) ").lower()
    if answer == "yes":
        print("Galat jawab aapne road cross nahi ki thi")
    else:
        print("aapne saman nahi giraya tha badam khaya kariye pata nahi kaha dhyaan h")

