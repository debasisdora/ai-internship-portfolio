employes=[
     {"name":"neha","salary":45000},
     {"name":"rakesh","salary":50000},
     {"name":"deb","salary":28000},
     {"name":"milu","salary":29000}
]
result={
    employe["name"]:employe["salary"] for employe in employes if employe["salary"]>=30000
}
print(result)