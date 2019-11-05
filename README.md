# Simple login flask application

## Usage

```bash
$ git clone https://github.com/shutdown57/login.git
$ pip install -r requirements.txt
```
Change username, password and database name in ```config.py``` file

Run in debug mode 
** Windows ```set DEBUG=1```
** Linux and Mac
```bash
$ export DEBUT=1
```

Then: ```FLASK_APP="src:create_app('Development')" flask run```

### Shell Context
```bash
$ FLASK_APP="src:create_app('Development')" flask shell
```

### Docker
If you use postgresql database with docker:
```bash
$ docker-compose -f develop-compose.yaml up
```
