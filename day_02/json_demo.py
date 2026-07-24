import json

with open("student.json",'r')as file:
    data =json.load(file)
print(f'student: {data['name']}')
print(f'python marks: {data['subjects']['python']}')
data['internship']['company']="nielit ai internship progam"
data['internship']['start_date']="2026-07-15"

with open("student_updated.json","w")as file:
    json.dump(data,file,indent=2)

print("\n updated record saved to student_updated.json")