a = b = 1
c = 0
sum_ = 0

while sum_ < 4000000 :
    c = a+b
    if not c%2 : sum_ += c
    a,b = b,c

print(sum_ - c)
