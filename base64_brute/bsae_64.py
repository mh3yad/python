import base64
import random
import string
chars=['zg5','zND','MTI','U2N']     
random.shuffle(chars)
print(chars)
a="".join(chars)+"MAo="               
print(a)
data = base64.b64decode(a+"==")
print(data)




