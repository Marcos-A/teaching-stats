import json


class JsonSerializable(object):
    def toJson(self):
        # Add option "ensure_ascii=False" for utf-8 encoding
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.toJson


class UserEvaluation(JsonSerializable):
    def __init__(self, email, degree_id):
        self.email = email
        self.level_id = None
        self.level_name = None
        self.degree_id = degree_id
        self.classgroup_id = None
        self.classgroup_name = None
        self.subjects = None
        self.evaluations = {}

    def __init__(self, email, level_id, level_name, degree_id, classgroup_id, classgroup_name, subjects):
        self.email = email
        self.level_id = level_id
        self.level_name = level_name
        self.degree_id = degree_id
        self.classgroup_id = classgroup_id
        self.classgroup_name = classgroup_name
        self.subjects = subjects
        self.evaluations = {}

    def __str__(self):
        return (self.email + ', ' + self.level_id +
                ', ' + self.level_name + ', ' + self.degree_id +
                ', ' + self.classgroup_id + ', ' + self.classgroup_name +
                ', ' + self.subjects + ', ' + self.evaluations)

    def __repr__(self):
        return 'UserEvaluation(email=%s, level_id=%s, level_name=%s, degree_id=%s, classgroup_id=%s, classgroup_name=%s, subjects=%s)' %\
               (self.email, self.level_id, self.level_name, self.degree_id, self.classgroup_id, self.classgroup_name, self.subjects)
