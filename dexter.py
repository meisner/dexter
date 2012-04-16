#!/usr/bin/python

class ExperimentController(object):
    def __init__(self, constructor, worker, destructor):
        self.constructor = constructor
        self.worker = worker
        self.destructor = destructor

    def run(self):
        self.constructor()
        self.worker()
        self.destructor()

def main():
  print HEADER
  CreateDatabse('./test.dex')

if __name__ == '__main__':
    main()
