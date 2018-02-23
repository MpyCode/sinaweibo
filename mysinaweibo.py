from sinaweibo import APIClient
import webbrowser
APP_KEY='3243500318'
APP_SECRET='e76746078f23dcc6485c36b0b7e805c2'
CALLBACK_URL='https://api.weibo.com/oauth2/default.html'
client=APIClient(app_key=APP_KEY,app_secret=APP_SECRET,redirect_uri=CALLBACK_URL)
url=client.get_authorize_url()
print(url)
webbrowser.open_new(url)

print('输入code')
code=input()
r=client.request_access_token(code)
access_token=r.access_token
expires_in=r.expires_in

client.set_access_token(access_token,expires_in)
statuses=client.statuses__public_timeline()['statuses']
length=len(statuses)
print(length)
for i in range(0,length):
    print('昵称'+statuses[i]['user']['screen_name'])
    print('简介'+statuses[i]['user']['description'])
    print('位置'+statuses[i]['user']['location'])
    print('微博'+statuses[i]['text'])
