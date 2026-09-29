from collections import deque

def countStudents(students, sandwiches):
    queue = deque(students)

    for sandwich in sandwiches:
        found = False

        for i in range(len(queue)):
            student = queue.popleft()

            if student == sandwich:
                found = True
                break
            else:
                queue.append(student)

        if not found:
            break

    return len(queue)

print(countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))