from datetime import datetime

from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class schoolSchool(models.Model):
    _name = "school.school"

    name = fields.Char('School Name')
    logo = fields.Binary(string="School Logo")
    tagline = fields.Char(string="Tag Line")
    tags = fields.Char('Achivements')
    area = fields.Char(string="Area")
    city = fields.Char('City')
    State_id = fields.Many2one('res.country.state', 'State')
    Country_id = fields.Many2one('res.country', 'Country')


    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100):

        if args is None:
            args = []
        recs = self.search(['|', ('name', operator, name), ('area', operator, name)] + args, limit=limit)
        return recs.name_get()

    @api.multi
    def name_get(self):
        res = []
        for field in self:
            res.append((field.id, '%s (%s)' % (field.name, field.area)))
        return res

    # def name_search(self, name, args=None, operator='ilike', limit=100):
    #     args = args or []
    #     recs = self.browse()
    #     if name:
    #         recs = self.search([('number', '=', name)] + args, limit=limit)
    #     if not recs:
    #         recs = self.search([('name', operator, name)] + args, limit=limit)
    #     return recs.name_get()



