"""
Given a list of projects and a list of dependencies of the projects,
find the order of building projects such that there is no error. 
If build is not possible, return -1
"""
from collections import defaultdict

projects = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]


def build_graph(projects, dependencies):
    graph = {proj: [] for proj in projects}
    for proj, proj_dep in dependencies:
        graph[proj].append(proj_dep)

    # print(graph.keys())
    return graph


def do_dfs(project):
    global order, graph, state
    print(f'DFS on project {project}')
    if state[project] == 'visiting':
        # A cycle is detected
        return False

    state[project] = 'visiting'
    for node in graph[project]:
        if state[node] == '':
            if not do_dfs(node):
                return False

    state[project] = 'visited'
    order.append(project)
    return True


def build_order(projects, dependencies):
    for project in projects:
        # Do a DFS for each project
        # Check if the project has been already visited state or not
        if state[project] == '':
            if not do_dfs(project):
                return False

    return True


order = []
state = defaultdict(str)
graph = build_graph(projects, dependencies)

if build_order(projects, dependencies):
    print(order[::-1])
else:
    print(state, order)
    print('Cannot complete dependencies: Cycle found')
