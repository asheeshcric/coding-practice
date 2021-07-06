"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
"""


def create_graph(num_courses, prerequisites):
    # first, create an empty graph for each course
    graph = {i: [] for i in range(num_courses)}
    for course, prereq in prerequisites:
        graph[course].append(prereq)

    return graph


def is_possible(num_courses, graph):
    # intuitively, we will need to find if there is a cycle in the graph or not
    visit_set = set()

    def dfs(course):
        if course in visit_set:
            # We are already visiting this course and found a cycle
            return False

        if not graph[course]:
            # Since it does not have any prereq, we can take this course
            return True

        visit_set.add(course)
        for neighbor in graph[course]:
            if not dfs(neighbor):
                return False

        # Finally, we know that we can take this course. So, we need to remove it from the visit set
        visit_set.remove(course)
        # Making prereq empty as we already know that this can be taken
        graph[course] = []
        return True

    # Now, checking the same thing for all courses manually as the graph may not be fully connected
    for course in range(num_courses):
        if not dfs(course):
            return False

    return True


if __name__ == "__main__":
    num_courses = 2
    prerequisites = [[1, 0]]
    # This means to complete course "1", you must complete course "0" first
    graph = create_graph(num_courses, prerequisites)
    print(is_possible(num_courses, graph))
