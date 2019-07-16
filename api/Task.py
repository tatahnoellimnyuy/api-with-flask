from flask_restful import Resource
import logging as logger

class Task(Resource):
	def get(self):
		logger.debug("inside GET method")
		return {"message":"inside GET method"},200

	def post(self):
		logger.debug("inside POST method")
		return {"message":"inside POST method"},200

	def put(self):
		logger.debug("inside PUT method")
		return {"message":"inside PUT method"},200

	def delete(self):
		logger.debug("inside DELETE method")
		return {"message":"inside DELETE method"},200
		