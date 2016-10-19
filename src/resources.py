from models import Repo
from db import session
from flask_restful import reqparse, abort, Resource, fields, marshal_with
from flask import request
repo_fields = {
    "id" : fields.Integer,
    "name": fields.String,
    "creation_date": fields.DateTime,
    "creator" : fields.String,
    "access_cnt": fields.Integer
}

parser = reqparse.RequestParser()
parser.add_argument('creator', type=str)
parser.add_argument('name', type=str)

class RepoResource(Resource):

    @marshal_with(repo_fields)
    def get(self,id):
        repo = session.query(Repo).filter(Repo.id == id).first()
        self.increment_cnt(repo)
        if not repo:
            abort(404, message="[ERROR] - Repo {} doesn't exist".format(id))
        return repo

    def delete(self, id):
        repo = session.query(Repo).filter(Repo.id == id).first()
        if not repo:
            abort(404, message="[ERROR] - Repo {} doesn't exist".format(id))
        session.delete(repo)
        session.commit()
        return {}, 204

    def increment_cnt(self, repo):
        repo.access_cnt = int(repo.access_cnt) + 1
        session.add(repo)
        session.commit()


class RepoListResource(Resource):

    @marshal_with(repo_fields)
    def get(self):
        cnt = request.args.get('cnt')
        if cnt is None:
            repos = session.query(Repo).all()
        else:
            repos = session.query(Repo).filter(Repo.access_cnt >= cnt ).all()
        return repos

    @marshal_with(repo_fields)
    def post(self):
        parsed_args = parser.parse_args()
        repo = Repo( creator=parsed_args['creator'], name=parsed_args['name'])
        session.add(repo)
        session.commit()
        return repo, 201

