#!/usr/bin/python
from client import Repoclient
import sys
import argparse
from dotenv import Dotenv

class CMD(object):
    def __init__(self):
        self.APIaddress = None
        self.args = None

    def setAddr(self):
        try:
            cmd_conf = Dotenv('./cmd-conf')
            self.APIaddress = cmd_conf['APIaddress']
            print cmd_conf['APIaddress']
        except IOError:
            env = os.environ

    def setparser(self):
        parser = argparse.ArgumentParser(
               description='Command line interface to repository manager')
        parser.add_argument('-d','--delete',
               help='Deletes a repository. Give the repository ID to delete it.',
               required=False,
               nargs=1,
               type=int,
               metavar=('REPOID'))

        parser.add_argument('-c','--create',
               help='Creates a new repository. First parameter is repository '\
               'name second is the creator name',
               required=False,
               nargs=2,
               type=str,
               metavar=('REPONAME', 'CREATOR'))

        parser.add_argument('-g', '--get',
              help='Get details about a repo. Give the repo ID.',
              required=False,
              nargs=1,
              type=int,
              metavar=('REPOID'))

        parser.add_argument('-l', '--list',
              help='List the available repositories. Optional value is'\
              ' an integer, if specified only the those repositories will be'\
              ' listed where number of accesses equals or greater than this.',
              required=False,
              nargs='?',
              type=int,
              const=0,
              default=-1,
              action='store',
              dest='cnt',
              metavar=('INT'))

        self.args = parser.parse_args()

    def choose(self, args):
        r = Repoclient(self.APIaddress)
        if args.delete:
            print 'To delete: {}'.format(args.delete[0])
            r.deleteRepo(args.delete[0])
        if args.create:
            print 'Create: {}\t{}'.format(args.create[0], args.create[1])
            r.createRepo(args.create[0], args.create[1])
        if args.get:
            print 'Get repodetails:\t{}'.format(args.get[0])
            res = r.getRepoDetails(args.get[0])
            r.printRepoDetails(res)
        if args.cnt > 0:
            res = r.getRepolist( cnt = args.cnt)
            r.printRepolist(res)
        if args.cnt == 0:
            res = r.getRepolist()
            r.printRepolist(res)

    def run(self):
        self.setAddr()
        self.setparser()
        self.choose(self.args)

if __name__ == '__main__':
    c =CMD()
    c.run()

