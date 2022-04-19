
students =[{'ssn':'401','name':'Zack','major':'Statistics'}, {'ssn':'402','name':'Raymond','major':'robotics'}]

print(f"Here are the student's list:{students}")

print("The sorted list is as below: ")
def sort_students(students):
    return sorted(students, key= lambda x: x['name'] )

print(sort_students(students))


#   sorted_students= sorted(students, ) 

#   print(f"The list of sorted students is:{sorted_students}")


