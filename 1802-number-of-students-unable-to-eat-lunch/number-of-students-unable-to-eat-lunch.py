class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counter = 0 
        while students and sandwiches:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                counter = 0 
                print("sandwich",sandwiches)
                print('students',students)
                print()
            else:
                stu = students.pop(0)
                students.append(stu) 
                print('sandwich',sandwiches)
                print("students",students)
                print()
                if counter == len(students):
                    break
                counter += 1   

        return len(students)    
        