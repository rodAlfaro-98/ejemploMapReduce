def Map(documents: list) -> list:
    list = []
    for i in range(len(documents)):
        for j in documents[i]:
            pair = (j,i)
            list.append(pair)
    return list

def Reduce(list: list) -> dict:
    map = {}
    for i in list:
        words = i[0].split(' ')
        for j in words:
            if j in map.keys():
                map[j].append(i[1])
            else:
                map[j] = [i[1]]
    return map