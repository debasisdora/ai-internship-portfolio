from datetime import date
def save_experiment_log(experiment_name,accuracy):
    data=open("experiment.log","a")
    data.write(f"{date.today()} | model: {experiment_name} | accuracy: {accuracy}\n")
    data.close()

save_experiment_log("logistic regrasion",0.91)
save_experiment_log("difrential eqation",0.45)
save_experiment_log("decision tree",0.86)

with open("experiment.log","r") as file:
    content=file.read()
print(content)