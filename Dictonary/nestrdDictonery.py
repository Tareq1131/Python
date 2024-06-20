student = {
    'name ': 'Tareq islam',
    'sub' : {
        'java' : 85,
        'js' : 86,
        'python' : 88,
    }

}

# print(student['sub'])
# print(student['sub']['python'])
print(student.keys())
print(list(student.keys()))
# for length 
print(len(list(student.keys())))

print(student.items())
# type cust
print(list(student.items()))

pairs = list(student.items())
print(pairs[0])
print(student.get('sub'))

student.update({'city' : 'dhaka'})
"""new version
new_dec = { 'city' : 'dhaka', 'age' : 26}
student.update(new_dec)"""
print(student)