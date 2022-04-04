import json
import datetime
import requests
import time

# exceptional moniter
def send_dingding_msg1(content, robot_id='钉钉机器人ID'): #please change to your own DingTalk ID
    try:
        msg = {
            "msgtype": "text",
            "text": {"content": content + '\n' + datetime.datetime.now().strftime("%m-%d %H:%M:%S")}
        }
        headers = {"Content-Type": "application/json ;charset=utf-8 "}
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_id
        body = json.dumps(msg)
        status = requests.post(url, data=body, headers=headers)
        if status.status_code == 200:
            return status.json()
        return status
    except Exception as err:
        print('Message unsent', err)

while True:
    try:
        url ="https://api.alternative.me/fng/?limit=0&format=json&date_format=cn"
        response = requests.get(url)
        if response.text:
            FGI =float(response.json()['data'][0]['value'])# processing data
            print('FGI', FGI)
            value_classification = response.json()['data'][0]['value_classification']
            print('value_classification:', value_classification)
            timestamp = response.json()['data'][0]['timestamp']
            print('timestamp', timestamp)
        else:
            continue
        if FGI <=20:# remind if it's smaller than 20
            print('FGI', FGI)
            content ='FGI is '+str(FGI) + ', which is smaller than the fixed bottom figure.'
            send_msg1 = send_dingding_msg1(content)
            print(send_msg1)
            break
        if FGI > 80:  # remind when it's larger than 80
            print('FGI', FGI)
            content = 'FGI is '+str(FGI) + ', which is larger than the fixed up figure.'
            send_msg1 = send_dingding_msg1(content)
            print(send_msg1)
    except Exception as order_err:\
            print("Keep trying", order_err)
    time.sleep(86400)

