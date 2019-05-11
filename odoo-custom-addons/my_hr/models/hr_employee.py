from odoo import models,fields
class EmployeeInherit(models.Model):
    _inherit = "hr.employee"
    miltiary_certificate = fields.Binary()
    job_title = fields.Char(required=True)

