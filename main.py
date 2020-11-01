from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
api = Api(app)

SERVER = '172.16.1.104,1433\LGEDSQL'
DATABASE = 'Mydatabase'
DRIVER = 'SQL Server'
USERNAME = 'sa'
PASSWORD = '12122012@Asif'
DATABASE_CONNECTION = f'mssql://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION
db = SQLAlchemy(app)


class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Video(name={self.name}, views={self.views}, likes={self.likes})"


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}


class VideoAll(Resource):
    @marshal_with(resource_fields)
    def get(self):
        result = VideoModel.query.all()
        if not result:
            abort(404, message='Could not find video with that id....')
        return result

    @marshal_with(resource_fields)
    def post(self):
        # args = request.get_json()
        args = video_update_args.parse_args()
        # result = VideoModel.query.all()
        # if result:
        #     abort(409, message='Video id taken...')
        video = VideoModel(name=args['name'], views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return 'Successful', 201


@marshal_with(resource_fields)
@app.route('/add_video', methods=['POST'])
def add_video():
    args = request.get_json()
    video = VideoModel(name=args['name'], views=args['views'], likes=args['likes'])
    db.session.add(video)
    db.session.commit()
    return 'Successful', 201


class Video(Resource):
    # @marshal_with(resource_fields)
    # def get(self, video_id):
    #     result = VideoModel.query.filter_by(id=video_id).first()
    #     if not result:
    #         abort(404, message='Could not find video with that id....')
    #     return result

    # @marshal_with(resource_fields)
    # def put(self, video_id):
    #     args = video_put_args.parse_args()
    #     result = VideoModel.query.filter_by(id=video_id).first()
    #     if result:
    #         abort(409, message='Video id taken...')
    #     video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
    #     db.session.add(video)
    #     db.session.commit()
    #     return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id....cannot update')

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        db.session.commit()

        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message='Could not find video with that id....cannot delete')
        db.session.delete(result)
        db.session.commit()
        return '', 204


api.add_resource(Video, "/video/<int:video_id>")

api.add_resource(VideoAll, "/videos")
# api.add_resource(VideoAll.post, "/videoput")


@marshal_with(resource_fields)
@app.route('/get')
def get():
    result = VideoModel.query.all()
    videos = []
    for video in result:
        videos.append({'name': video.name, 'likes': video.likes, 'views': video.views})

    return jsonify({'videoss': videos})


@marshal_with(resource_fields)
def put(self, video_id):
    args = video_put_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if result:
        abort(409, message='Video id taken...')
    video = VideoModel(id=video_id, name=args['name'], views=args['views'], likes=args['likes'])
    db.session.add(video)
    db.session.commit()
    return video, 201


@marshal_with(resource_fields)
def patch(self, video_id):
    args = video_update_args.parse_args()
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
        abort(404, message='Could not find video with that id....cannot update')

    if args['name']:
        result.name = args['name']
    if args['views']:
        result.views = args['views']
    if args['likes']:
        result.likes = args['likes']

    db.session.commit()

    return result


def delete(self, video_id):
    result = VideoModel.query.filter_by(id=video_id).first()
    if not result:
        abort(404, message='Could not find video with that id....cannot delete')
    db.session.delete(result)
    db.session.commit()
    return '', 204


if __name__ == "__main__":
    app.run(debug=True)
