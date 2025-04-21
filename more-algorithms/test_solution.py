import pytest
import solution


@pytest.mark.parametrize(
    'numCourses, prerequisites, has_solution', [
        (1, [], True),
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (3, [], True),
        (3, [[1,0],[2,1]], True),
        (4, [[1,0],[2,0],[3,1],[3,2]], True),
        (4, [[1,0],[2,0],[3,1],[3,2],[0,3]], False),
        (5, [[1,0],[2,0],[4,3]], True),
        (5, [[1,0],[2,0],[3,4]], True),
        (10, [[0,2],[2,4],[3,1],[4,9],[6,8],[8,4],[9,5]], True),
    ]
)
def test_course_schedule(numCourses, prerequisites, has_solution):
    order = solution.Solution().findOrder(numCourses, prerequisites)

    if has_solution:
        msg = f'Answer did not include all courses for numCourses {numCourses} and prerequisites {prerequisites}. Got: {order}.'
        assert len(order) == numCourses, msg
        assert all(i in order for i in range(numCourses)), msg

        prereq = {}
        for course, dep in prerequisites:
            prereq.setdefault(course, []).append(dep)
        took = set()
        for course in order:
            assert all(dep in took for dep in prereq.get(course, [])), f'Course {course} was taken before some of its prerequisites for numCourses {numCourses} and prerequisites {prerequisites}. Got: {order}.'
            took.add(course)
    else:
        assert order == [], f'Answer for numCourses {numCourses} and prerequisites {prerequisites} should be an empty list. Got: {order}.'
