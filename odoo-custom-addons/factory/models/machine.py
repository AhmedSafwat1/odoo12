from odoo import models,fields,api
from datetime import date, datetime
import requests
class Machine(models.Model):
    _name =  "factory.machine"
    name      =fields.Char()
    is_active =fields.Boolean()

    def json_rpc(self):
        resp = requests.get(
            "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=EGP&apikey=HY18FM7WZPM7CS78")
        return float(resp.json()['Realtime Currency Exchange Rate']['5. Exchange Rate'])

    @api.depends('cost')
    def compute_tax(self):
       for record in self:
           record.taxt = record.cost / self.json_rpc()
    image = fields.Binary()
    taxt = fields.Float(compute=compute_tax,store=True)
    date_now = fields.Datetime(string='Last Update',default=lambda self: fields.datetime.now())
    cost = fields.Integer()
    department_id = fields.Many2one("factory.department")
    tags_ids = fields.Many2many("factory.machine.tags")
    is_open = fields.Boolean(related="department_id.is_accept",store=True)
    state = fields.Selection([("dr","Drafat"),("act","Active"),("acc","accept")],default="dr")
    def valid(self):
        self.state = 'act'
    def accept(self):
        self.state = 'acc'
    def draft(self):
        self.state = 'dr'

class Tags(models.Model):
    _name = "factory.machine.tags"
    name = fields.Char()