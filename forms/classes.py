import json


class JsonSerializable(object):
    def toJson(self):
        # Add option "ensure_ascii=False" for utf-8 encoding
        return json.dumps(self.__dict__, ensure_ascii=False)

    def __repr__(self):
        return self.toJson


class UserEvaluation(JsonSerializable):
    def __init__(self, id, degree_id):
        self.id = id
        self.level_id = None
        self.level_code = None
        self.degree_id = degree_id
        self.group_id = None
        self.subjects = None
        self.evaluations = {}

    def __init__(self, id, level_id, level_code, degree_id, group_id, subjects):
        self.id = id
        self.level_id = level_id
        self.level_code = level_code
        self.degree_id = degree_id
        self.group_id = group_id
        self.subjects = subjects
        self.evaluations = {}

    def __str__(self):
        return (self.id + ', ' + self.level_id + ', ' + self.level_code +
                ', ' + self.degree_id + ', ' + self.group_id +
                ', ' + self.subjects + ', ' + self.evaluations)

    def __repr__(self):
        return 'UserEvaluation(id=%s, level_id=%s, level_code=%s, degree_id=%s, group_id=%s, subjects=%s)' %\
               (self.id, self.level_id, self.level_code, self.degree_id, self.group_id, self.subjects)
