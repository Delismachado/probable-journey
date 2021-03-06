from typing import Type
from flask_restful import Resource
from flask import request
from src.dao.base_dao import BaseDao


class BaseResource(Resource):
    def __init__(self, dao: BaseDao, type_model: Type):
        self.__dao = dao
        self.__model_type = type_model

    def get(self, id = None):
        if id:
            return self.__dao.read_by_id(id)
        return self.__dao.read_all()

    def post(self):
        data = request.json
        item = self.__model_type(**data)
        self.__dao.save(item)

        return item, 201

    def put(self, id):
        data = request.json

        if data['id'] == id:
            item = self.__dao.read_by_id(id)
            for key, value in data.items():
                setattr(item, key, value)

            return self.__dao.save(item)
        return None, 404

    def delete(self, id):
        item = self.__dao.read_by_id(id)
        self.__dao.delete(item)
        return None, 204
