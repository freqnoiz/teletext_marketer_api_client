Teletext Marketer sms gateway api client

Required python modules:

- requests


Standalone:
```
usage: textmarketer-sms-client.py [-h] [-u USERNAME] [-p PASSWORD] [-s SENDER]
                                  [-r RECIPIENT] [-m MESSAGE]

optional arguments:
  -h, --help            show this help message and exit

  -u USERNAME, --username USERNAME
                        Api username

  -p PASSWORD, --password PASSWORD
                        Api password

  -s SENDER, --sender SENDER
                        Sender ID
 
  -r RECIPIENT, --recipient RECIPIENT
                        Recipient
 
  -m MESSAGE, --message MESSAGE
                        Message
```

As module:
```
from textmarketer_sms_client import TMapi

client = TMapi(username='username', password='password')
client.send_sms(sender='Sender ID',recipient='447766554433',message='This is a sample message')
```

result:

```
> SUCCESS
> 1423
>

```
