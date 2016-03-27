#!/usr/bin/python
import sys
import random
import reg
def main():
    
    f_check = open('mails.txt').read()
    while len(f_check) > 2:
        
        f = open('mails.txt', 'r')
        f_non_liked = open('non-liked-mails.txt', 'a')
        f_reg = open('registred-mails.txt', 'a')
        random.seed()
        mail = f.readline()
        names_file = open('names.txt', 'r').readlines()
        images_file = open('images.txt', 'r').readlines()
        name = names_file[0][:-1]
        image = images_file[0][:-1]
        try:
            reg.main(['reg.main', mail, 'defPass', name, image])
            f_non_liked.write(mail)
            f_reg.write(mail)
        except:
            log = 'exc'

        f.close()

        f=open('names.txt').readlines()
        f.pop(0)
        with open('names.txt','w') as F:
            F.writelines(f)

        
        f=open('mails.txt').readlines()
        f.pop(0)
        with open('mails.txt','w') as F:
            F.writelines(f)

        f_reg.close()
        f_non_liked.close()

        f_check = open('mails.txt').read()
    
if __name__ == "__main__":
    sys.exit(main())
