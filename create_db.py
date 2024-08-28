from app_db import app,db, Student

with app.app_context():
    db.create_all()


    joshua = Student('Joshua',2,'male',1000)
    nicole = Student('Nicole',45,'female',1000)
    herbert = Student('Herbert',32,'male',1000)
    jalilu = Student('Jalilu',12,'male',1000)
    pokua = Student('Pokua',15,'female',1000)
    albert = Student('Albert',50,'male',1000)

    db.session.add_all([joshua,nicole,herbert,jalilu,pokua,albert])
    db.session.commit()