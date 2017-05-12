# -*- coding: utf-8 -*-

import os, random, signal, socket, sys, time

BUFFER_SIZE = 128
HOST = '127.0.0.1'
PORT = 4000

def cleanup():
  try:
    os.unlink(SOCKET_PATH)
  except OSError:
    return

def handle_sigint(signal, frame):
  cleanup()
  quit()

def serve():
  cleanup()

  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind((HOST, PORT))
  sock.listen(1)
  print "Waiting for new connection."

  conn, addr = sock.accept()

  while True:
    try:
      conn.sendall(str(random.random()))
      res = conn.recv(BUFFER_SIZE)
      print res
      time.sleep(0.1)
    except IOError:
      conn.close()
      print "Disconnected"
      serve()
      break

if __name__ == '__main__':
  sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)
  signal.signal(signal.SIGINT, handle_sigint)

  serve()
