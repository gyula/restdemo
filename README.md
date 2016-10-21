# This a Demo restful application
Demo repository manager application, the whole application running in docker containers.

## Client Usage
- -h, --help            show this help message and exit
- -d REPOID, --delete REPOID:Deletes a repository. Give the repository ID to delete it.
- -c REPONAME CREATOR, --create REPONAME CREATOR :Creates a new repository. First parameter is repository name second is the creator name
- -g REPOID, --get REPOID: Get details about a repo. Give the repo ID.
- -l [INT], --list [INT] :List the available repositories. Optional value is an integer, if specified only the those repositories will be listed where number of accesses equals or greater
than this.
## Example
- Create reposiroty: python cmd.py -c "Example repo name" "Jon Smith"
- List repository: python cmd.py --list
- List repositories with more than 5 accesses: python cmd.py --list 5
- Delete repository: python cmd.py --delete 6
- Get details about a specific repo: python cmd.py --get 1

## Deployment
- client cmd-conf contains the Server Address example config: APIaddress = 'http://client:5000' if you choosed other names, rename the name of the container!
You have to link the two containers, container names will be also visible in /etc/hosts (inside the containers). After the containers running simply use docker attach CONTAINERID inside the /code you will find the application.

OR

- Run build.sh script.

### Example
- Build docker files:
- docker build -t server .
- docker build -t client .
- Start server container: docker run -t -p 5000:5000 --name server server
- Start the client container and link them: docker run -it --link server:client --name clientest client bash

## Tests
execute nosetests command
