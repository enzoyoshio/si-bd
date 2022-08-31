from marshmallow import Schema, fields

class LoginSchema(Schema):
    id=fields.Int(),
    usuaio=fields.Str(),
    senha=fields.Str(),
