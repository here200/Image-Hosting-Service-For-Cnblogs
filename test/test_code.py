import xmlrpc.client as mwb

with open('./images/人.png', 'rb') as f:
    picture_data = f.read()

file = {
    'bits': picture_data,
    'name': '人.png',
    'type': 'png'
}

params = {
    'blogid': '', # 暂时没有任何用处，随便写
    'username': '',
    'password': '',
    'file': file
}

proxy = mwb.ServerProxy(uri="")
url_data = proxy.metaWeblog.newMediaObject(params['blogid'], params['username'], params['password'], params['file'])
print(url_data)
