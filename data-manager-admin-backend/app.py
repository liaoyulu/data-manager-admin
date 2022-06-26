from unittest import result
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jtl.db'

db = SQLAlchemy(app)
api = Api(app)

# RESTFUL API


class NoticeApi(Resource):
    def get(self, notice_id):
        notice = Notice.query.filter_by(noticeId=notice_id).first()
        result = {
            'noticeId': notice.noticeId,
            'noticeTitle': notice.noticeTitle,
            'noticeContent': notice.noticeContent,            
        }
        return jsonify(result)

    def put(self, notice_id):
        notice = Notice.query.filter_by(noticeId=notice_id).first()
        if notice is None:
            notice = Notice(
                noticeTitle = request.form['noticeTitle'],
                noticeContent=request.form['noticeContent'],                
            )
            db.session.add(notice)
            db.session.commit()
            return f'add {notice.noticeId} {notice.noticeTitle} success'
        else:
            notice.noticeTitle = request.form['noticeTitle']
            notice.noticeContent = request.form['noticeContent']
            db.session.commit()
            return f'update {notice.noticeId} {notice.noticeTitle} success'            

    def delete(self, notice_id):
        notice = Notice.query.filter_by(noticeId=notice_id).first()
        if Notice is None:
            return f'delete error, not found {notice_id}'
        else:
            db.session.delete(notice)
            db.session.commit()
            return f'delete {notice.noticeId} success'

api.add_resource(NoticeApi, '/api/notice/<int:notice_id>')

class StuffApi(Resource):
    def get(self, stuff_id):
        stuff = Stuff.query.filter_by(stuffId=stuff_id).first()
        result = {
            'stuffId': stuff.stuffId,
            'userName': stuff.userName, 
            'stuffName': stuff.stuffName,
            'sex': stuff.sex,
            'birthDate': stuff.birthDate,    
        }
        return jsonify(result)

    def put(self, stuff_id):
        stuff = Stuff.query.filter_by(stuffId=stuff_id).first()
        if stuff is None:
            stuff = Stuff(
                userName = request.form['userName'],   
                stuffName = request.form['stuffName'],  
                sex = request.form['sex'], 
                birthDate= request.form['birthDate'],              
            )
            db.session.add(stuff)
            db.session.commit()
            return f'add {stuff.stuffId} {stuff.stuffName} success'
        else:
            stuff.userName = request.form['userName']   
            stuff.stuffName = request.form['stuffName']
            stuff.sex = request.form['sex']
            stuff.birthDate= request.form['birthDate']            
            db.session.commit()
            return f'update {stuff.stuffId} {stuff.stuffName} success'            

    def delete(self, stuff_id):
        stuff = Stuff.query.filter_by(stuffId=stuff_id).first()
        if Stuff is None:
            return f'delete error, not found {stuff_id}'
        else:
            db.session.delete(stuff)
            db.session.commit()
            return f'delete {stuff.stuffId} success'

api.add_resource(StuffApi, '/api/stuff/<int:stuff_id>')

class SearchApi(Resource):
    def get(self, search_method):
        if search_method == 'Notice':
            if request.form['searchField'] == 'noticeId':
                notice = Notice.query.filter_by(noticeId=request.form['searchValue']).all()
            elif request.form['searchField'] == 'noticeTitle':
                notice = Notice.query.filter(
                    Notice.noticeTitle.like("%" + request.form['searchValue'] + "%") if request.form['searchValue'] is not None else ""
                    ).all()
            else:
                return f"not this field {request.form['searchField']}"
            if notice is not None:
                listResult = []
                for i in notice:
                    result = {
                        'noticeId': i.noticeId,
                        'noticeTitle': i.noticeTitle,
                        'noticeContent': i.noticeContent,
                    }
                    listResult.append(result)
                return jsonify(listResult)
            else:
                return 'None'
        elif search_method == 'Stuff':
            stuff = Stuff.query.filter_by(stuffName=request.form['searchValue']).all()
            stuffcount =Stuff.query.filter_by(stuffName=request.form['searchValue']).count()
            print(stuffcount)
            listResult = []
            if stuff is not None:
                for i in stuff:
                    result = {
                        'stuffId': i.stuffId,
                        'userfName': i.userName,  
                        'stuffName': i.stuffName,
                        'sex': i.sex,
                        'birthDate': i.birthDate,    
                    }
                    listResult.append(result)
                return jsonify(listResult)
                   
api.add_resource(SearchApi, '/api/search/<string:search_method>')

# SQLAlchemy Model
class Notice(db.Model):
    noticeId = db.Column(db.Integer, primary_key=True)
    noticeTitle = db.Column(db.String(120), unique=False, nullable=False)
    noticeContent = db.Column(db.Text(1024), unique=False, nullable=False)

    def __repr__(self):
        return f'<Notice {self.noticeId} {self.noticeTitle}>'

class Stuff(db.Model):
    stuffId = db.Column(db.Integer, primary_key=True)
    userName = db.Column(db.String(120), unique=False, nullable=False)
    stuffName = db.Column(db.String(120), unique=False, nullable=False)
    sex = db.Column(db.String(8), unique=False, nullable=False)
    birthDate = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<Stuff {self.stuffId} {self.userName} {self.stuffName} {self.sex} {self.birthDate}  >'


if __name__ == '__main__':
    app.run(debug=True)