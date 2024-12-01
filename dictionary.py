dict = {}
dict1={"name":"John","grade":12}
dict2={1:"apple",2:"banana"}
dict3={"name":"jack",2:[3,4,5]}
dict4={"name":"sonia","age":16}
print(dict4["name"])
print(dict4["age"])
dict4["age"]=18
print(dict4)
dict4["address"]="rwanda"
print(dict4)
dict4.pop("age")
print(dict4)
print("address",dict4.get("address"))
dict4.clear()
print(dict4)