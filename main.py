List1 = [1,1,2]
List2 = [0, 0,1, 1, 1, 2, 2, 3, 3, 4]
List3 = [1,1,2,3,3,5,6,6,6,6,6,6,6,8,8,9,10,10,11,14,20,25,25,26,26,26]

def duplicates_remover(list):

    temp = []

    for x in list:
        if x not in temp:
            temp.append(x)

    print(temp)


duplicates_remover(List1)

duplicates_remover(List2)

duplicates_remover(List3)
