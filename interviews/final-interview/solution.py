from collections import deque

def findOrder(numCourses, prerequisites):
    """
    Returns a valid order in which to complete all courses given the prerequisites.

    Uses topological sorting (Kahn's algorithm) to determine a possible ordering.
    If no valid ordering exists (i.e., there is a cycle), returns an empty list.

    Time: O(V + E), where V is the number of courses and E is the number of prerequisite pairs
    Space: O(V + E), for the adjacency list and in-degree storage
    """
    graph = [[] for _ in range(numCourses)]
    in_degree = [0] * numCourses

    for a, b in prerequisites:
        graph[b].append(a)
        in_degree[a] += 1

    queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
    course_order = []

    while queue:
        course = queue.popleft()
        course_order.append(course)

        for neighbor in graph[course]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(course_order) != numCourses:
        return []

    return course_order
