from odoo import models, fields, api, exceptions, _
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT

class SchoolSubjectsAvailable(models.Model):
    _name = "school.subjects.available"

    name = fields.Selection([('1st std', '1st std'), ('2nd std', '2nd std'),
                                           ('3th std', '3th std'), ('4th std', '4th std'),
                                           ('5th std', '5th std'), ('6th std', '6th std'),
                                           ('7th std', '7th std'), ('8th std', '8th std'),
                                           ('9th std', '9th std'), ('10th std', '10th std'),
                                           ('11th std', '11th std'), ('12th std', '12th std')], string='Standard', required=True)
    school_id = fields.Many2one('school.school', string="School", required=True)
    subject1 = fields.Char('subject1')
    subject2 = fields.Char('subject2')
    subject3 = fields.Char('subject3')
    subject4 = fields.Char('subject4')
    subject5 = fields.Char('subject5')