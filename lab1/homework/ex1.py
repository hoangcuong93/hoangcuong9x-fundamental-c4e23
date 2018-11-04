from gmail import GMail, Message
from random import choice
import datetime
gmail = GMail("spy12a6@gmail.com","cuong11a6")
message = Message("Don xin nghi", to="cuongnh1305.namtien@gmail.com", text="em bi dau bung")
now = datetime.datetime.now()
n = now.hour, now.minute
timer = "07:00"
while True:
    if timer !=n:
        gmail.send(message)
        break