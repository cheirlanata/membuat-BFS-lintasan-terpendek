peta = { 
    'A': set (['B']),
    'B': set (['C','D']), 
    'C': set (['B','E']),
    'D': set (['B','G','H']),
    'E': set (['C','F','G']),
    'F': set (['E']),
    'G': set (['D','E','I','J']),
    'H': set (['D','J']),
    'I': set (['G']),
    'J': set (['G','H']),
}

def bfs_lintasan_terpendek(peta, mulai, tujuan):
    explored = []
    queue = [[mulai]]
    
    if mulai == tujuan :
        return "Awal adalah Tujuan"
    
    while queue :
        jalur = queue.pop(0)
        node =  jalur[-1]
        
        if node not in explored : 
            neighbours = peta[node]
            
            for neighbour in neighbours :
                jalur_baru = list(jalur)
                jalur_baru.append(neighbour)
                queue.append(jalur_baru)
                
                if neighbour == tujuan:
                    return jalur_baru
                
            explored.append(node)
            
    return "Mohon maaf node yang kalian pilih tidak ada"

mulai = input("Masukkan nilai awal :  ")
tujuan =  input("Masukkan nilai tujuan : ")

print(bfs_lintasan_terpendek(peta, mulai, tujuan)) 