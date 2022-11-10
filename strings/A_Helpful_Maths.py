s = input()
lst = list(map(int,s.split("+")))
lst.sort()
lst = [str(i) for i in lst]
print("+".join(lst))