from collections import defaultdict

class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            in_degree[a] += 1

        stack = [i for i in range(numCourses) if in_degree[i] == 0]
        course_order = []

        while stack:
            course = stack.pop()
            course_order.append(course)

            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)

        if len(course_order) != numCourses:
            return []

        return course_order
