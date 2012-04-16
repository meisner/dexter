#!/usr/bin/python

import sqlite3

HEADER = "Welcome to the lab"

def main():
  print HEADER
  CreateDatabse('./test.dex')

def CreateDatabse(filename):
  conn = sqlite3.connect(filename)

  c = conn.cursor()

  # Create table
  c.execute('''create table experiments (uid)''')
  c.execute('''insert into experiments values (1)''')

  # Save (commit) the changes
  conn.commit()

  # We can also close the cursor if we are done with it
  c.close()

def LoadDatabase(filename):
  pass

def GetMachineInfo(hostname):
  print "Getting machine info for %s" % (hostname)

main()
