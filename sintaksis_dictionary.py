users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "addres": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }

}
print(users)
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print(users["addres"])
print(users["addres"]["street"])
print(users["addres"]["geo"]["lat"])
print(users["addres"]["geo"]["lng"])

print("\nUbah dict ke json")
print(users)
print("\nCara Cek type data")
print(type(users))

print("\nCara ubah ke JSON")
import json
result = json.dumps(users)
print("\nCek type data dari result")
print(type(result))
print(result)

with open('result.json','w') as file:
    json.dump(users, file)