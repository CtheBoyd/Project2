#5 Author: Christopher Boyd
# GitHub username: CtheBoyd
# Date: 4/5/2022
# Description: Asks user to provide an amount under one dollar and returns the change required.
#
print ("Please enter an amount in cents less than a dollar.")
change = float(input())
q = (change // 25)
qr = (change % 25)
d = (qr // 10)
dr = (qr % 10)
n = (dr // 5)
nr = (dr % 5)
p = (nr // 1)
print ("Your change will be:")
print ("Q:", q)
print ("D:", d)
print ("N:", n)
print ("P:", p)
