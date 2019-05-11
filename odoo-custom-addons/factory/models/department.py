from odoo import models,fields
class Department(models.Model):
    _name =  "factory.department"
    name      =fields.Char()
    is_accept =fields.Boolean()
    desc = fields.Html()
    details = fields.Text()
    machine_ids = fields.One2many("factory.machine","department_id")
    log_ids = fields.One2many("factory.department.machine.log","department_id")

