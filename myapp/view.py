import requests
from myapp import db
from myapp.models import User, Posts, Comments, Albums, Photos, Todos


response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()

responses = requests.get ('https://jsonplaceholder.typicode.com/posts')
posts = responses.json()

responses = requests.get ('https://jsonplaceholder.typicode.com/comments')
comments = responses.json()

responses = requests.get ('https://jsonplaceholder.typicode.com/albums')
albums = responses.json()

responses = requests.get ('https://jsonplaceholder.typicode.com/photos')
photos = responses.json()

responses = requests.get ('https://jsonplaceholder.typicode.com/todos')
todos = responses.json()



for records in data:
    users_details = User(
                        id = records['id'],
                        name = records['name'],
                        username = records['username'],
                        email = records['email'],
                        address = records['address'],
                        phone = records['phone'],
                        website = records['website'],
                        company = records['company']
                    )
    db.session.add(users_details)

for record in posts:
    posts_details = Posts(
                        userId = record['userId'], 
                        id = record['id'],
                        title = record['title'],
                        body = record['body']
                        )
    db.session.add(posts_details)
for record in comments:
    comments_details = Comments(
                        postId = record['postId'], 
                        id = record['id'],
                        name = record['name'],
                        email = record['email'],
                        body = record['body']
                        )
    db.session.add(comments_details)
for record in albums:
    albums_details = Albums(
                        userId = record['userId'], 
                        id = record['id'],
                        title = record['title']
                        )
    db.session.add(albums_details)
for record in photos:
    photos_details = Photos(
                        albumId = record['albumId'], 
                        id = record['id'],
                        title = record['title'],
                        url = record['url'],
                        thumbnailUrl = record['thumbnailUrl']
                        )
    db.session.add(photos_details)
for record in todos:
    todos_details = Todos(
                        userId = record['userId'], 
                        id = record['id'],
                        title = record['title'],
                        completed = record['completed']
                        )
    db.session.add(todos_details)
    db.session.commit()
