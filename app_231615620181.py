from collections import deque

def bfs_shortest_path(city_map, start, goal):
    if start == goal:
        return [start]

    queue = deque([[start]])  # Antrian BFS
    visited = set()

    while queue:
        path = queue.popleft()  # Ambil jalur pertama
        node = path[-1]  # Ambil node terakhir dari jalur
        
        if node not in visited:
            neighbors = city_map.get(node, [])
            
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                
                if neighbor == goal:
                    return new_path  # Rute terpendek ditemukan
            
            visited.add(node)  # Tandai node sebagai dikunjungi

    return None  # Jika tidak ada jalur ditemukan

# Contoh Penggunaan
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

start = 'Home'
goal = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, goal)
print("Shortest path:", shortest_path)
