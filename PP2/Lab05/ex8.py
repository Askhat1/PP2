import re
txt="python_Aegex_Aweqweqwe"
a = re.findall('[A-Z][^A-Z]*', txt)
x=a
print(x)