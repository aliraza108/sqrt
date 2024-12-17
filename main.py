b = int(input("what is your b: "))
a = int(input("what is your a: "))
c = int(input("what is your c: "))

ans = -b + (b*b - (4*a*c)) **0.5 / (2*a)
ans1 = -b - (b**2 - (4*a*c)) **0.5 / (2*a)
print(ans)
 
 # long method
 
# a = int(input("what is your a: "))
# b = int(input("what is your b: "))
# c = int(input("what is your c: "))

# bminus = - b
# bsqr = b**2
# ac4 = 4*a*c
# a2 = 2*a
# sqrt1 = (bsqr - ac4)**(1/2)
# final1 = (bminus + sqrt1) / a2
# final2 = (bminus - sqrt1) / a2


