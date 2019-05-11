from odoo import models,fields

class Log(models.Model):
    _name =  "factory.department.machine.log"
    # _rec_name = " machine_id.name"
    note      =fields.Text()
    machine_id = fields.Many2one("factory.machine")
    department_id = fields.Many2one("factory.department")
    date_note = fields.Datetime(string='Last Update',default=lambda self: fields.datetime.now())
