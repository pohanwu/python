a=["retention",3,None]
b=["retention",3,None]
print(a is b)
b=a
print(a is b)
a="Something"
b=None
print(a is not None,b is None)
a=2
b=6
print(a==b)
print(a<b)
print(a<=b,a!=b,a>=b,a>b)
a="many paths"
b="many paths"
print(a is b)
print(a==b)
a=9
print(0<=a<=10)
"three"<4

