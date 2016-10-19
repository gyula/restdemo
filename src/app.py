#!/usr/bin/env python

from flask import Flask
from flask_restful import Api
from resources import RepoListResource
from resources import RepoResource

app = Flask(__name__)
api = Api(app)

api.add_resource(RepoListResource, '/repos', endpoint='repos')
api.add_resource(RepoResource, '/repos/<string:id>', endpoint='repo')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
