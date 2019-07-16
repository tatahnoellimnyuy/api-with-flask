from flask_restful import Api
from app import flaskAppInstance
from .Task import Task
from .TaskByID import TaskByID

rest_server=Api(flaskAppInstance)
rest_server.add_resource(Task,"/api/v1.0/task/")
rest_server.add_resource(TaskByID,"/api/v1.0/task/id/<string:taskid>")
