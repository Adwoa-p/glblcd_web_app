from app_db import app,db, Student

with app.app_context():
    db.create_all()


    joshua = Student('Joshua',2,'male')
    nicole = Student('Nicole',45,'female')
    herbert = Student('Herbert',32,'male')
    jalilu = Student('Jalilu',12,'male')
    pokua = Student('Pokua',15,'female')
    albert = Student('Albert',50,'male')

    db.session.add_all([joshua,nicole,herbert,jalilu,pokua,albert])
    db.session.commit()