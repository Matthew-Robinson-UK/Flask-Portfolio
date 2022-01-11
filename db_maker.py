from blog import db
from blog.models import Post, User, Comment, Rating

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

db.drop_all()
db.create_all()

user1 = User(
    email="user1@test.ac.uk", password="passuser1"
)
user2 = User(
    username = 'Matthew', email="robinson.matthew2@gmail.com", linkedin = 'https://www.linkedin.com/in/matthew-lee-robinson/', password = 'admin', is_admin=1
)


post1 = Post(title="Post 1", content="12345", description="123", author_id=2)
post2 = Post(title="Post 2", content="12345", description='123', author_id=2)
post3 = Post(title="Post 3", content="12345", description='123', author_id=2)

comment = Comment(comment='test', author_id=2, post=post1)
rating = Rating(value='5', author_id=2, post=post1)

db.session.add(user1)
db.session.add(user2)
db.session.add(post1)
db.session.add(post2)
db.session.add(post3)

db.session.commit()