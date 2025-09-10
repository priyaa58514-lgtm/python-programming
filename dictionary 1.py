d={"emno":123,"emname":"abc"}
print(d)
print(d["emno"])
print(d.get("emname"))
d["emname"]="priya"
print(d)
d["age"]=18
for key in d:
    print(key)
for key,value in d.items():
    print(key, ":",value)
d.pop("emno")
print(d)
