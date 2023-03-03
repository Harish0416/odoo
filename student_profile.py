from odoo import models, fields, api, _
from datetime import date, datetime
from odoo.exceptions import ValidationError


class Schoolstudentprofile(models.Model):
    _name = "school.student.profile"

    Student_Image = fields.Binary('Student Image', required=True)
    date_time = fields.Datetime('Date Time')
    Student_Name = fields.Char('Student Name', required=True)
    Last_Name = fields.Char('Last Name', required=True)
    DOB = fields.Date('DOB', required=True)
    age = fields.Integer("Age", required=True)
    Gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True)
    Adress = fields.Char('Adress', required=True)
    Street1 = fields.Char('Street 1', required=True)
    Street2 = fields.Char('Street 2', required=True)
    City = fields.Char('City', required=True)
    State_id = fields.Many2one('res.country.state', 'State', required=True)
    Country_id = fields.Many2one('res.country', 'Country', required=True)
    Pincode = fields.Integer('PIN', required=True)
    Parent_Name = fields.Char('Parent Name', required=True)
    Last_Name = fields.Char('Last Name', required=True)
    Relation_To_Student = fields.Selection([('father', 'Father'), ('mother', 'Mother'),
                                            ('garden', 'Garden')], string="Relation To Student", required=True)
    Telno = fields.Integer('Tel.no.', required=True)
    Email = fields.Char('Email', required=True)
    Phnno = fields.Integer('Phn.no.', required=True)
    Parent_Sign = fields.Binary('Parent Sign', required=True)
    Student_Sign = fields.Binary('Student Sign', required=True)
    state = fields.Selection([('draft', 'Draft'), ('inprogress', 'In-progress'), ('validate', 'Validate'),
                              ('approved', 'Approved')], default='draft', string='Status')

    def action_inprogress(self):
        if self.state == 'draft':
            self.state = 'inprogress'

    def action_validate(self):
        if self.state == 'inprogress':
                self.state = 'validate'

    def action_approve(self):
        if self.state == 'validate':
            self.state = 'approved'

    @api.onchange("DOB")
    def onchange_age(self):
        if self.DOB:
            today = date.today()
            today_year = today.year
            d = datetime.strptime(self.DOB, '%Y-%m-%d').date()
            dob_year = d.strftime("%Y")
            self.age = today_year - int(dob_year)