#dictionary
dict={
    "name":"srishti",
    "cgpa":8.5,
    "place":"ghaziabad"
}
print(dict)

print(dict["name"])

dict["cgpa"]=8.6
print(dict)

dict["key"]="value"
print(dict)

#Null Dictionary
null_dict={}
print(null_dict)

#Nested dictionary
student={
    "name":"sri",
    "score":{
        "chem":98,
        "phy":96,
        "maths":94
    }
}
print(student["score"]["maths"])

#dictionary methods
print(student.keys())
print(student.values())
print(list(student.keys()))
print(list(student.values()))
student.items()
print(student)
print(student.get("score"))

print(student.get("name"))
newstud={
    "name":"shruti"
}
print(student.update(newstud))
print(student)