import requests

headers = {
    'Content-Type': 'application/json',
    'Postman-Token': '55661366-e7e1-4276-bebd-54b945640054',
    'cache-control': 'no-cache',
}

index = 0
while True:	
	data = '{"garantia":' + '"'+ str(index) + '" }'
        print(data)
	response = requests.post('http://localhost:8000/alta_garantia', headers=headers, data=data)
	index += 1
