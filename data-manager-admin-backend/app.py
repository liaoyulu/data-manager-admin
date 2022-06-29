from unittest import result
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import time

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jtl.db'

db = SQLAlchemy(app)
api = Api(app)


####### Notice
class Notice(db.Model):
    noticeId = db.Column(db.Integer, primary_key=True)
    noticeTitle = db.Column(db.String(120), unique=False, nullable=False)
    noticeContent = db.Column(db.Text(1024), unique=False, nullable=False)
    noticeReadnum = db.Column(db.Integer, unique=False, nullable=False)
    noticeDate = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<Notice {self.noticeId} {self.noticeTitle}>'
    

class Staff(db.Model):
    staffId = db.Column(db.Integer, primary_key=True)
    staffUserName = db.Column(db.String(120), unique=False, nullable=False)
    staffName = db.Column(db.String(120), unique=False, nullable=False)
    staffSex = db.Column(db.String(8), unique=False, nullable=False)
    staffBirthDate = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return f'<Staff {self.staffId} {self.staffUserName} {self.staffName} {self.staffSex} {self.staffBirthDate}  >'
    
#### RESTFUL API
class NoticeApi(Resource):
    def get(self, notice_id):
        notice = Notice.query.filter_by(noticeId=notice_id).first()
        result = {
            'noticeId': notice.noticeId,
            'noticeTitle': notice.noticeTitle,
            'noticeContent': notice.noticeContent,
            'noticeReadnum' : notice.noticeReadnum,
            'noticeDate' : notice.noticeDate,
        }
        return jsonify(result)

    def put(self, notice_id):
        # 0 表示添加数据，其他表示更新数据
        if notice_id == 0:
            notice = Notice(
                noticeTitle = dict(request.json)['noticeTitle'],
                noticeContent = dict(request.json)['noticeContent'],  
                noticeReadnum = 0,
                noticeDate = dict(request.json)['noticeDate'],                                
            )
            db.session.add(notice)
            db.session.commit()
            return f'通知 {notice.noticeId} {notice.noticeTitle} 发布成功'
        else:
            notice = Notice.query.filter_by(noticeId=notice_id).first()
            if notice is None:
                return f'not found {notice.noticeId}'
            else:
                notice.noticeTitle = dict(request.json)['noticeTitle'],
                notice.noticeContent = dict(request.json)['noticeContent'],  
                print(notice.noticeTitle)
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

class StaffApi(Resource):
    # def get(self, staff_id):
    #     staff = Staff.query.filter_by(staffId=staff_id)
    #     listResult = []
    #     if staff is not None:
    #         for i in staff:
    #             result = {
    #                     'staffId': i.staffId,
    #                     'staffUserName': i.staffUserName,  
    #                     'staffName': i.staffName,
    #                     'staffSex': i.staffSex,
    #                     'staffBirthDate': i.staffBirthDate,    
    #                 }
    #             listResult.append(result)
    #         return jsonify(listResult)

    # def put(self, staff_id):
    #     staff = Staff.query.filter_by(staffId=staff_id).first()
    #     if staff is None:
    #         staff = Staff(
    #             staffUserName = request.form['staffUserName'],   
    #             staffName = request.form['staffName'],  
    #             staffSex = request.form['staffSex'], 
    #             staffBirthDate= request.form['staffBirthDate'],              
    #         )
    #         db.session.add(staff)
    #         db.session.commit()
    #         return f'add {staff.staffId} {staff.staffName} success'
    #     else:
    #         staff.staffUserName = request.form['staffUserName']   
    #         staff.staffName = request.form['staffName']
    #         staff.staffSex = request.form['staffSex']
    #         staff.staffBirthDate= request.form['staffBirthDate']            
    #         db.session.commit()
    #         return f'update {staff.staffId} {staff.staffName} success'            

    def delete(self, staff_id):
        staff = Staff.query.filter_by(staffId=staff_id).first()
        if Staff is None:
            return f'delete error, not found {staff_id}'
        else:
            db.session.delete(staff)
            db.session.commit()
            return f'delete {staff.staffId} success'

api.add_resource(StaffApi, '/api/staff/<int:staff_id>')

class NoticeListApi(Resource):
    def get(self):
        notices = Notice.query.all()
        result = []
        for notice in notices:
            result.append(
                {
                    'noticeId': notice.noticeId,
                    'noticeTitle': notice.noticeTitle,
                    'noticeContent': notice.noticeContent,
                    'noticeReadnum': notice.noticeReadnum,
                    'notiecDate' : notice.noticeDate,
                }
            )
        return jsonify(result)

api.add_resource(NoticeListApi, '/api/notice_list')

class StaffListApi(Resource):
    def get(self):
        staffs = Staff.query.all()
        print(staffs)
        result = []
        for staff in staffs:
            item={
                    'staffId': staff.staffId,
                    'staffName': staff.staffName,
                    'staffUserName': staff.staffUserName,
                    'staffSex': staff.staffSex,
                    'staffBirthDate': staff.staffBirthDate,
                }
            result.append(item)
        return jsonify(result)


api.add_resource(StaffListApi, '/api/staff_list')


class NoticeSearchByTitleApi(Resource):
    def post(self):
        title = dict(request.json)['noticeTitle']
        search_query = "%{}%".format(title['_rawValue'])
        notices = Notice.query.filter(Notice.noticeTitle.like(search_query)).all()
        result = []
        for notice in notices:
            result.append(
                {
                    'noticeId': notice.noticeId,
                    'noticeTitle': notice.noticeTitle,
                    'noticeContent': notice.noticeContent,
                    'noticeReadnum': notice.noticeReadnum,
                    'notiecDate' : notice.noticeDate,
                }
            )
        return jsonify(result)

api.add_resource(NoticeSearchByTitleApi, '/api/notice_search_by_title')

class StaffSearchByNameApi(Resource):
    def post(self):
        name = dict(request.json)['staffName']
        search_query = "%{}%".format(name['_rawValue'])
        staffs = Staff.query.filter(Staff.staffName.like(search_query)).all()
        result = []
        for staff in staffs:
            result.append(
                {
                    'staffId': staff.staffId,
                    'staffName': staff.staffName,
                    'staffUserName': staff.staffUserName,
                    'staffSex': staff.staffSex,
                    'staffBirthDate': staff.staffBirthDate,
                }
            )
        return jsonify(result)

api.add_resource(StaffSearchByNameApi, '/api/staff_search_by_name')


# SQLAlchemy Model



if __name__ == '__main__':
    app.run(debug=True)
