#!/usr/bin/env python
import os
import sys
import socket
 
for addr in sys.stdin:
  addr = addr.rstrip(os.linesep)
 
  try:
    internal = socket.inet_pton(socket.AF_INET6, addr)
    print socket.inet_ntop(socket.AF_INET6, internal)
 
  except socket.error:
    print "Invalid address"
