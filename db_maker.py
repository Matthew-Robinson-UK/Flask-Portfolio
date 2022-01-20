from blog import db
from blog.models import Post, User, Comment, Rating

# https://flask-sqlalchemy.palletsprojects.com/en/2.x/api/

# db.drop_all()
db.create_all()

user1 = User(
    username = '', email="user1@test.ac.uk", password="passuser1"
)
user2 = User(
    username = 'Matthew', email="robinson.matthew2@gmail.com", linkedin = 'https://www.linkedin.com/in/matthew-lee-robinson/', password = '1Admin2854', is_admin=1
)


post1 = Post(title="Professional Athlete", content="In 2012 I first joined the British team as a professional athlete and through my career got to race at 7 World Championships, 8 European Championships and The World Univeristy Games. I am the current british record holder in the k4 500m, the event you can see in the image above (I am in the back of the boat!) and managed to achieve a top 5 finish at the World Cup in 2018 along with a Top 8 finish in the 2016 European Championships. Whilst I'm very pround of all these achievements it is the skills and experience I picked up from working towards these goals which is the most valuable. Some of these included managing a challenging schedule of training, competing and also studying so as to continually improve and achieve success not just in sport but all areas of my life. A record of resilience and determination, setting challenging goals and working towards them over multiple years. Using initiative to find ways to improve through researching areas such as psychology, performance analysis, biometrics and training methodologies. Strong team work and leadership skills through taking on leader roles in the squads i trained with as well as working with a team of coaches and support staff to fine tune every aspect of my performance.", description="For 8 years I had a career as a professional athete in the sport of Sprint Kayaking. I was a member of the British team and had the honour of competing for Great Britain at 7 World Championships.", author_id=2, image_file='athlete.jpg')
post2 = Post(title="Vaccination Co-ordinator and Administrator", content="In 2020 I joined my local surgery as a Vaccine Co-ordinator, it was a role I took to help improve the situation with the pandemic in my local area. It involved aiding a team of nurses and manager in streamlining the administration process at vaccine clinics, working to bring 5 min appointment times down to 2 mins to deal with the increasing demands of the pandemic. Using problem solving skills to become familiar with new software and systems used by the NHS whilst also working remotely to provide further support during Flu clinics. Provide technical support and train new administrators, dealing with problems in a fast and efficient manner, prioritising tasks and ensuring an effective service for the patients. Scheduling and co-ordinating clinics in advance to ensure the most effecient use of time and resources.", description='During the start of the pandemic I took on the role of Vaccination Co-ordinator and Administrator at my local surgery, to help support the increased pressure put on the NHS due to the Covid-19 virus.', author_id=2, image_file='vaccine.jpg')
post3 = Post(title="Technical Coach ", content="In 2021 I decided to give back some of the knowledge I had learned as an athlete to the young athletes working towards similar goals in South Wales. As the Canoe Wales technical Coach I have planned and scheduled weekly training up to 6 months to a year in advance, ensuring a successful strategy is set out for them to succeed. Managed groups of up to 12 athletes of varied abilities, adapting communication and coaching styles to make sure each one can achieve their best. Provided comprehensive feedback and analysis on their technical and physical abilites as well as coaching them in skills learnt through being an athlete on how to become successful in all areas. I have had the opportunity to learn from some great leaders over my professional life and I am now continuing to develop those skills through constantly trying to be a capable and reliable leader myself", description='I am currently the Canoe Wales technical coach for the Junior Welsh sprint group, taking the skills and experience I built up during my time as an athlete and passing them on to aspiring young competitors.', author_id=2, image_file='coaching.jpg')

# comment = Comment(comment='Example Comment', author_id=2, post=post1)
# rating = Rating(value='5', author_id=2, post=post1)

# db.session.add(user1)
# db.session.add(user2)
# db.session.add(post1)
# db.session.add(post2)
db.session.add(post3)


db.session.commit()