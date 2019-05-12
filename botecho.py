from flask import Flask
from flask_restful import Api, Resource
from farmware_tools import device


class Echo(Resource):
  def get(self, crap):
    return crap, 200

  def post(self):
    pass

  def put(self):
    pass

  def delete(self):
    pass


class Move(Resource):
  def get(self, crap):
    pass

  def post(self, x, y, z):
    try:
      return device.move_relative(x, y, z, 10), 200
    except Exception as ex:
      return str(ex), 500

  def put(self):
    pass

  def delete(self):
    pass

try:
  app = Flask("FB Test")
  api = Api(app)
  api.add_resource(Echo, "/echo/<string:crap>")
  api.add_resource(Move, "/move/<int:x>/<int:y>/<int:z>")
  app.run(port=8081)
except Exception as error:
  device.log(repr(error))


