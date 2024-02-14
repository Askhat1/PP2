def uniq(x):
    only_uniq = [1]
    for i in x:
        if i not in only_uniq:
            only_uniq.append(i)
    print(only_uniq)
inpt = input()
x = inpt.split()
uniq(x)