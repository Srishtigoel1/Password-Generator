import random 
#generating random password for suggestions
uppercase="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase=uppercase.lower()
digits="0123456789"
symbols="!@#$%^&*()_+{|[]\-><,.?/}~`"
upper,lower,nums,syms=True,True,True,True

all=""
if upper:
    all+=uppercase
if lower:
    all+=lowercase
if nums:
    all+=digits
if syms:
    all+=symbols
#print(all)
length=20 #length of the password 
# amount=10 #Number of password to generate
# for x in range(amount):
#     password="".join(random.sample(all,length))
#     print(password)
#     print("\n")

#printing only one
for x in range(1):
    password="".join(random.sample(all,length))
    print(password)
    print("\n")

