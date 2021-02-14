import json


class JsonSerializable(object):
    def toJson(self):
        # Add option "ensure_ascii=False" for utf-8 encoding
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.toJson


class UserEvaluation(JsonSerializable):
    def __init__(self, email, degree):
        self.email = email
        self.level = None
        self.degree = degree
        self.classgroup = None
        self.subjects = None
        self.evaluations = {}

    def __init__(self, email, level, degree, classgroup, subjects):
        self.email = email
        self.level = level
        self.degree = degree
        self.classgroup = classgroup
        self.subjects = subjects
        self.evaluations = {}

    def __str__(self):
        return (self.email + ', ' + self.level + ', ' + self.degree +
                ', ' + self.classgroup + ', ' + self.subjects+ ', ' + self.evaluations)

    def __repr__(self):
        return 'UserEvaluation(email=%s, level=%s, degree=%s, classgroup=%s, subjects=%s)' %\
               (self.email, self.level, self.degree, self.classgroup, self.subjects)
