import json
import requests
from prettytable import PrettyTable

class Repoclient(object):

    def __init__(self, APIaddress):
        self.APIaddress = APIaddress
        self.headers={'Content-Type': 'application/json'}

    def getRepolist(self, cnt = None):
        try:
            rUrl = self.APIaddress + '/repos'
            if cnt is not None:
                rUrl = '{}?cnt={}'.format(rUrl, cnt)
            response = requests.get(rUrl)
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            print err
            response = None
        return response

    def createRepo(self, rName, rCreator):
        try:
            rUrl = self.APIaddress + '/repos'
            print rName,rCreator
            response = requests.post(
                          rUrl,
                          headers=self.headers,
                          data=json.dumps({ u'creator': rCreator,
                                            u'name': rName }))
            print response
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            print err
            response = None
        return response

    def deleteRepo(self,repoID):
        try:
            response = requests.delete(self.APIaddress + '/repos/' + str(repoID))
            response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print err
            response = None
        return response

    def getRepoDetails(self,repoID):

        try:
            response = requests.get(self.APIaddress + '/repos/' + str(repoID))
            response.raise_for_status()
            response = response.json()
        except requests.exceptions.HTTPError as err:
            print err
            response = None
        return response


    def printRepolist(self, response):
        if response is not None:
            t = PrettyTable(["ID", "Repository Name", "Creator"])
            for item in response:
                t.add_row([item['id'], item['name'], item['creator']])
            print t

    def printRepoDetails(self, response):
        if response is not None:
            t = PrettyTable(['Repository', ''])
            t.add_row(['id', response['id']])
            t.add_row(['Name', response['name']])
            t.add_row(['Creator', response['creator']])
            t.add_row(['Created', response['creation_date']])
            t.add_row(['Accessed', response['access_cnt']])
            print t

