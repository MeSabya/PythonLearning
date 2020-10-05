import requests

class Blog:
    def __init__(self, name):
        self.name = name

    def posts_timeout(self):
        print("Posts is called")
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            return response.json()
        except:
            raise requests.exceptions.Timeout


    def posts(self):
        print("Posts is called")
        try:
            response = requests.get("https://jsonplaceholder.typicode.com/posts")
            return response.json()
        except:
            return "Some exception received"


    def __repr__(self):
        return '<Blog: {}>'.format(self.name)