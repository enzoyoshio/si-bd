from marshmallow import Schema, fields

# nao usei, dps perguntar para o guto
class AreaSchema(Schema):
    id=fields.Int(),
    latitude=fields.Float(),
    longitude=fields.Float(),
    nome=fields.Str(), 
    descricao=fields.Str(), 
    lotacao_max=fields.Int(), 
    modalidade=fields.Str(),
    horario_seg=fields.Str(),
    horario_ter=fields.Str(),
    horario_qua=fields.Str(),
    horario_qui=fields.Str(),
    horario_sex=fields.Str(),
    horario_sab=fields.Str(),
    horario_dom=fields.Str()