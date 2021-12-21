from blog import db
from blog.models import Post, User

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

db.drop_all()
db.create_all()

user1 = User(
    username="johnsmith",
    email="johnsmith@gmail.com",
)


post1 = Post(title="Post 1", content="12345", author_id=1)
post2 = Post(title="Post 2", content="12345", author_id=1)


db.session.add(user1)
db.session.add(post1)
db.session.add(post2)

db.session.commit()