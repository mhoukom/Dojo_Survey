from flask.helpers import flash
from flask_app.config.mysqlconnection import connectToMySQL
from flask import Flask, session


class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']

    @classmethod
    def save(data):
        query = """INSERT into surveys (name, location, language, comment) 
                    VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"""

        return connectToMySQL('dojo_survey').query_db(query, data)


@classmethod
def get_last_survey():
    query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
    results = connectToMySQL('dojo_survey').query_db(query)

    return Survey(results[0])


@staticmethod
def is_valid(survey):
    is_valid = True
    if len(survey['name']) < 2:
        flash("Name must be at least 2 characters.")
    if len(survey['location']) <  2:
        is_valid = False
        flash("Must choose a location.")
    if len(survey['language']) <  2:
        is_valid = False
        flash("Must choose a language.")
    if len(survey['comment']) <  2:
        is_valid = False
        flash("Comments must be more than 2 characters.")
    return is_valid
