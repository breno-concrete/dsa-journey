from collections import deque

def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person[-1] == 'm':
                print(f'{person} has a mango!')
                return True
            else:
                searched.append(person)
                search_queue += graph[person]
    return False

graph = {}
graph["Breno"] = ["Alícia", "Bernardo", "Carol", "Caleam"]
graph['Alícia'] = ["Lusiana", "Francisco"]
graph["Francisco"] = ["Abraham"]
graph["Ana"] = ["Alícia"]
graph["Carol"] = []
graph["Bernardo"] = []
graph["Lusiana"] = []
graph["Abraham"] = []


search("Breno")
