# Course Schedule II (Topological Sort)

## Description

You are given a number `numCourses` representing the total number of courses you need to take, labeled from `0` to `numCourses - 1`. You are also given a list of prerequisite pairs. Each pair `[a, b]` indicates that in order to take course `a`, you must first complete course `b`.

Your task is to return an array that represents a valid order in which to take the courses. If there are multiple valid answers, return any of them. If it is impossible to complete all courses, return an empty array.

### Examples

**Example 1:**

```

Input: numCourses = 2, prerequisites = \[\[1,0]]
Output: \[0,1]

```

**Example 2:**

```

Input: numCourses = 4, prerequisites = \[\[1,0],\[2,0],\[3,1],\[3,2]]
Output: \[0,1,2,3] or \[0,2,1,3]

```

**Example 3:**

```

Input: numCourses = 1, prerequisites = \[]
Output: \[0]

```

### Constraints

- 1 ≤ numCourses ≤ 2000  
- 0 ≤ prerequisites.length ≤ numCourses × (numCourses - 1)  
- prerequisites[i].length == 2  
- 0 ≤ ai, bi < numCourses  
- ai != bi  
- All the pairs [ai, bi] are distinct

## Reference

This problem is adapted from LeetCode: [Course Schedule II](https://leetcode.com/problems/course-schedule-ii/).

## Hints

1. **Model the problem as a graph**: Treat each course as a node and each prerequisite pair `[a, b]` as a directed edge from `b` to `a`. This means you need to take course `b` before `a`.

2. **Build the graph and compute in-degrees**: Create an adjacency list to represent the graph and an array to store the in-degree (number of incoming edges) for each course.

3. **Use Kahn’s algorithm for topological sorting**: Initialize a queue with all nodes that have in-degree 0 (no prerequisites). Repeatedly remove a node from the queue, add it to the result, and reduce the in-degree of its neighbors. If any neighbor’s in-degree becomes 0, add it to the queue.

4. **Detect cycles**: If the number of courses in the result is less than `numCourses`, there must be a cycle in the graph, making it impossible to finish all courses.

## Solution (without code)

1. Model the courses and prerequisites as a directed graph.
2. Count the in-degree (number of incoming edges) for each node.
3. Initialize a queue with all nodes that have in-degree 0 (courses with no prerequisites).
4. While the queue is not empty:
   - Remove a course from the queue and add it to the result.
   - For each course dependent on it, reduce its in-degree by 1.
   - If any of these now have in-degree 0, add them to the queue.
5. If the resulting list contains all courses, return it. Otherwise, return an empty array.

[Click to see the online visualization.](https://claude.ai/public/artifacts/e368aa89-2719-4781-8763-424ea828d784)

## Time and Space Complexity

**Time Complexity**:  
O(V + E), where V is the number of courses and E is the number of prerequisites. We visit each node and edge once.

**Space Complexity**:  
O(V + E), to store the adjacency list and the in-degree array.
```
