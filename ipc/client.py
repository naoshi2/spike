# -*- coding: utf-8 -*-

import os, random, signal, socket, sys, time

BUFFER_SIZE = 128
HOST = '127.0.0.1'
PORT = 4000

def handle_sigint(signal, frame):
  quit()

def dial():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  try:
    sock.connect((HOST, PORT))
  except IOError:
    print "fatal: socket does not exist"
    return

  while True:
    try:
      data = sock.recv(BUFFER_SIZE)
      sock.send("ok")
      print "Received: %s" % repr(data)
    except IOError:
      sock.close()
      print "fatal: connection refused.."
      return

if __name__ == '__main__':
  sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
  signal.signal(signal.SIGINT, handle_sigint)

  dial()
