from marshmallow import Schema, fields, validate, ValidationError

# Customer Schema for Validation
class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    email = fields.Email(required=True)
    phone_number = fields.Str(required=True, validate=[validate.Length(min=10, max=15)])

# CustomerAccount Schema for Validation
class CustomerAccountSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True, validate=[validate.Length(min=5, max=20)])
    password = fields.Str(required=True, validate=[validate.Length(min=8)])

# Product Schema for Validation
class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=[validate.Length(min=1, max=100)])
    price = fields.Float(required=True)

# Order Schema for Validation
class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_id = fields.Int(required=True)
    items = fields.List(fields.Dict(keys=fields.Str(), values=fields.Int()), required=True)

# WorkoutSession Schema for Validation
class WorkoutSessionSchema(Schema):
    id = fields.Int(dump_only=True)
    member_id = fields.Int(required=True)
    session_date = fields.DateTime(required=True)
    duration = fields.Int(required=True)
