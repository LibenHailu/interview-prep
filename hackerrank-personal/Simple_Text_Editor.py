undo = [""]
for n in [*open(0)][1:]:
    
    q = n.split()
    if q[0] == "1":
        undo.append(undo[-1] + q[1])
    if q[0] == "2":
        undo.append(undo[-1][:-int(q[1])])
    if q[0] == "3" :
        i = int(q[1]) - 1
        print(undo[-1][i])
    if q[0] == "4":
        s = undo.pop()

    
    