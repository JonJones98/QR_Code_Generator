from unittest import result
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class Validate:
    @staticmethod
    def validate_info(QRinfo):
        is_valid = True # we assume this is true
        if len(QRinfo['url']) < 1:
            flash("*URL field is missing")
            is_valid = False
        if len(QRinfo['filename']) < 1:
            flash("*Filename is missing")
            is_valid = False
        if (QRinfo['formattype'])in "Select Format":
            flash("*Select Format type")
            is_valid = False
        return is_valid


