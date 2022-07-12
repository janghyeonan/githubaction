import requests, telegram
response = requests.get("https://www.clien.net/service/board/cm_iphonien")
if response.text.find(sys.argv[3]) != -1:    
    telegram.Bot(token=sys.argv[1]).send_message(chat_id=sys.argv[2], text='Clien Right now!!')
else:
    telegram.Bot(token=sys.argv[1]).send_message(chat_id=sys.argv[2], text='No~~!')
