from flask_restful import Resource
import logging as logger

class TaskByID(Resource):
	def get(self,taskid):
		logger.debug("inside GET method ... taskID={}".format(taskid))
		return {"message":"inside GET method ... taskID={}".format(taskid)},200

	def post(self,taskid):
		logger.debug("inside POST method ... taskID={}".format(taskid))
		return {"message":"inside POST method ... taskID={}".format(taskid)},200

	def put(self,taskid):
		logger.debug("inside PUT method ... taskID={}".format(taskid))
		return {"message":"inside PUT method ... taskID={}".format(taskid)},200

	def delete(self,taskid):
		logger.debug("inside DELETE method ... taskID={}".format(taskid))
		return {"message":"inside DELETE method ... taskID={}".format(taskid)},200
		