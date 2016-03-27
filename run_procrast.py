#!/usr/bin/python
import sys
import time
import random
import login_and_like_me
import login_and_like_random_rec

def main():
    period_like_me = 100
    iteration = 1
    random.seed()
    while 1:
        mail = random.choice([line for line in open('registred-mails.txt', 'r')])[:-1]
        password = 'defPass'
        random_post = random.randrange(1,622123,1)
        try:
            page = "http://www.livelib.ru/review/" + str(random_post)
            login_and_like_random_rec.main(['login_and_like_random_rec.py', mail, password, page])
        except:
            time.sleep(5)
        time.sleep(5)

if __name__ == "__main__":
    sys.exit(main())
