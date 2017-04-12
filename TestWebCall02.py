import TestWebCall01,requests

class TestWebCall02:

  def __init__(self,user,password):
    self.user = user
    self.password = password
    TestWebCall01()
    print("First Section was completed")
    r2 = requests.get('https://api.github.com/user', auth=('self.user', 'self.password'))
    print(r2.status_code)
    print(r2.headers['content-type'])
    print(r2.encoding)
    print(r2.text)
    print(r2.json())
    TestWebCall02('','')
