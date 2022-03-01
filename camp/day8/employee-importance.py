"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""


class Solution:
    def getImportanceDFS(self, employeeId, employeesAdjacencyMap, visited):
        visited.add(employeeId)
        subordinates, importance = employeesAdjacencyMap[employeeId]
        for subordinate in subordinates:
            if subordinate not in visited:
                importance += self.getImportanceDFS(
                    subordinate, employeesAdjacencyMap, visited)
        return importance

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        visited = set()
        employeesAdjacencyMap = {}

        for employee in employees:
            employeesAdjacencyMap[employee.id] = (
                employee.subordinates, employee.importance)

        return self.getImportanceDFS(id, employeesAdjacencyMap, visited)
