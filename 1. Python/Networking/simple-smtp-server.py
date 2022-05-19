from __future__ import print_function
from datetime import datetime
import asyncore
from smtpd import SMTPServer

class EmlServer(SMTPServer):
    no = 0
    def process_message(self, peer, mailfrom, rcpttos, data):
        filename = 'mail%s-%d.txt' %(datetime.now().strftime('%Y%m%d%H%M%S'),self.no)
        f = open(filename, 'w')
        f.write(mailfrom+'\n')
        f.write(rcpttos[0]+'\n')
        f.write(data)
        f.close
        print('%s saved.' % filename)
        self.no += 1


def run():
    # start the smtp server on 192.168.56.1:1025
    foo = EmlServer(('192.168.56.1', 1025),('localhost', 1025), map=None, decode_data=True)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    run()
