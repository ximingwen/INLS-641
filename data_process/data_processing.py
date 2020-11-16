import json

output=[]
with open('csvjson.json') as f:
	json_data = json.load(f)
	for data in json_data:
		precessed_data={}
		precessed_data["state"]=data["state"]
		precessed_data['scores']={}
		precessed_data['scores']['anger']=data["anger"]
		precessed_data['scores']['anticipation']=data["anticipation"]
		precessed_data['scores']['disgust']=data["disgust"]
		precessed_data['scores']['fear']=data["fear"]
		precessed_data['scores']['sadness']=data["sadness"]
		precessed_data['scores']['surprise']=data["surprise"]
		precessed_data['scores']['trust']=data["trust"]
		precessed_data['scores']['joy']=data["joy"]
		precessed_data['scores']['overall_sentiment']=data["overall_sentiment"]
		precessed_data['scores']['Time_Period']=data["date"]
		precessed_data['scores']['cases']=data['cases']
		output.append(precessed_data)
        

file = open('data.json','w',encoding='utf-8')
json.dump(output,file,ensure_ascii=False)

     