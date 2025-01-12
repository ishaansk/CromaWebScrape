import requests
response = requests.get("https://www.croma.com/croma-84-litres-2-star-direct-cool-single-door-refrigerator-with-stabilizer-free-operation-crlr084dcc290110-grey-/p/275249")
if response.status_code != 200:
    print("error")
    exit()
else:
    content = response.content
print(content)