def test(lst):
    result={}
    for item in lst:
        result[item[2]]=item[0:2]
    return result
students = [[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
print(students)
print(test(students))




