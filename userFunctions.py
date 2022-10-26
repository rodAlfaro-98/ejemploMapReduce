def Map(documents):
    list = []
    for i in range(len(documents)):
        for j in documents[i]:
            pair = (j,i)
            list.append(pair)
    return list

def Reduce(list):
    map = {}
    for i in list:
        words = i[0].split(' ')
        #print(words)
        for j in words:
            if j in map.keys():
                map[j].append(i[1])
            else:
                map[j] = [i[1]]
    return map