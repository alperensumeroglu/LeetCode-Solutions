
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Adjacency list to represent course dependencies
        course_dependencies = defaultdict(list)
        for prerequisite, course in prerequisites:
            course_dependencies[course].append(prerequisite)

        # DFS function to compute all prerequisites for a given course
        def find_prerequisites(course):
            if course not in prerequisite_map:
                prerequisite_map[course] = set()
                for prereq in course_dependencies[course]:
                    prerequisite_map[course] |= find_prerequisites(prereq)
                prerequisite_map[course].add(course)
            return prerequisite_map[course]

        # Map to store all prerequisites for each course
        prerequisite_map = {}
        for course in range(numCourses):
            find_prerequisites(course)

        # Evaluate each query based on the computed prerequisites
        result = []
        for start, end in queries:
            result.append(start in prerequisite_map[end])
        return result

''''

# Intuition
This problem can be solved by treating the courses and their prerequisites as a directed graph. 
To determine if one course is a prerequisite of another, we can compute the transitive closure 
of the graph using a depth-first search (DFS).

# Approach
1. Represent the courses and their prerequisites as an adjacency list.
2. Use a DFS-based approach to compute all indirect prerequisites for each course.
   - Maintain a map where each course points to the set of all its prerequisites (both direct and indirect).
3. For each query, check if the first course is present in the prerequisite set of the second course.

# Complexity
- Time complexity: O(V + E + Q), where V is the number of courses, E is the number of prerequisites, and Q is the number of queries.
  - Constructing the adjacency list takes O(E).
  - Running DFS for all courses takes O(V + E) in total.
  - Evaluating the queries takes O(Q).
- Space complexity: O(V^2), where V is the number of courses.
  - The prerequisite map may store up to O(V^2) pairs in the worst case.
'''