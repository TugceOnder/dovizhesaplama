import requests
import json
api_url =" https://api.exchangeratesapi.io/latest?base="
bozulan_doviz= input("Bozulan doviz turu : ")
alinan_doviz=input("alinan doviz türü: ")
miktar=int(input(f"Ne kadar {bozulan_doviz} bozdurmak istiyorsunuz "))
result= requests.get(api_url+bozulan_doviz)
result=json.loads(result.text)
print(result)
print("1 {0} = {1} {2}".format(bozulan_doviz,result["rates"][alinan_doviz],alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar,bozulan_doviz,miktar*result["rates"][alinan_doviz],alinan_doviz))