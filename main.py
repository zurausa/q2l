import requests as req


# line
lineurl = "https://notify-api.line.me/api/notify"
access_token = ''
headers = {'Authorization': 'Bearer ' + access_token}
geturl = ""


def getText():  # get Text
    tex = req.get(geturl)
    return tex


# send message
def sendText(tex):
    message = 'test'
    payload = {'message': message}
    req.post(lineurl, headers=headers, params=payload,)


# main
t = getText()
print(t)
# sendText(t)
