from RESTAPI import app,db
import requests
from RESTAPI.models import User



response = requests.get('https://jsonplaceholder.typicode.com/users')
data = response.json()


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
    db.create_all()
    db.session.add(users_details)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)