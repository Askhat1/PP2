import re
txt = "The rain in Spain abbb"
x = re.findall(r'a(b{2,3})', txt)
print(x)