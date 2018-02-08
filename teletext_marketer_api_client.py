import requests
import argparse


class TMapi:
    def __init__(self, username='', password='', https_proxy=''):
        self.https_proxy = https_proxy
        self.username = username
        self.password = password
        
    def send_sms(self, recipient='', message='', sender=''):
        data = {
            'username' : self.username,
            'password' : self.password,
            'to' : recipient,
            'message' : message,
            'orig' : sender
            }        
        if self.https_proxy == '':
            status = requests.get('https://api.textmarketer.co.uk/gateway/', params=data).text
        else:
            proxies = { 'https' : self.https_proxy }
            status = requests.get('https://api.textmarketer.co.uk/gateway/', proxies=proxies, params=data).text
        print(status)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--username", help="Api username", required=True)
    parser.add_argument("-p","--password", help="Api password", required=True)
    parser.add_argument("-s","--sender", help="Sender ID", required=True)
    parser.add_argument("-r","--recipient", help="Recipient", required=True)
    parser.add_argument("-m","--message", help="Message", required=True)

    args = parser.parse_args()
    tm_client = TMapi(username=args.username, password=args.password)
    tm_client.send_sms(recipient=args.recipient, message=args.message, sender=args.sender)


