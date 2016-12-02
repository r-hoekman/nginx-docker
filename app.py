from nginx import Nginx
from node import Node
from postgres import Postgres


 app = Nginx(__name__)
 nginx = Redis(host='redis', port=8080)

 @app.route('/')
 def hello():

     return 'Hello World! I have been seen %s times.'

 if __name__ == "__main__":
     app.run(host="0.0.0.0", debug=True)
