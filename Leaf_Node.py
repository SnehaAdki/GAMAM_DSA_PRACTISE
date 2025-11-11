def leaf_node_graph(trust):
    hash_map = {}
    for i in range(0,len(trust)):
        if trust[i][0] in hash_map.keys():
            hash_map[trust[i][0]] += hash_map[trust[i][0]]
        else:
            hash_map[trust[i][0]] =1
            
    print(hash_map)

    arr = []
    for i in range(0,len(trust)):
        if trust[i][1] not in hash_map.keys():
            if trust[i][1] not in arr:
                arr.append(trust[i][1])
        if trust[i][0] not in hash_map.keys():
            if trust[i][0] not in arr:
                arr.append(trust[i][0])
    
    print(arr)
    j = 0
    while j < len(arr):
        for i in range(0,len(trust)):
            if arr[j] == trust[i][1]:
                hash_map[trust[i][0]] -=1 
            if hash_map[trust[i][0]] == 0:
                del hash_map[trust[i][0]]
        j+=1

    
    return arr[0] if len(arr) > 0 else -1
    
        

trust = [[1,2],[2,3]]
print(leaf_node_graph(trust))
