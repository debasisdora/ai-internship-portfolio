import json
with open("student.json","r") as file:
    data=json.load(file)
    for subject,marks in data['subjects'].items():
        if marks >=40:
            result ="pass"
        else:
            result = "fail"
        print(f"{subject}: {marks}- {result}")
        overal_result='pass'
        if marks<40:
            overal_result="fail"
        report={
            "name":data["name"],
            "overal_result": overal_result
        }
        with open("student_report.json","w") as file:
            json.dump(report,file,indent=2)

