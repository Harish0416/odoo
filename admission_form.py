from odoo import models, fields, api, _
from datetime import date, datetime
from odoo.exceptions import ValidationError


class SchoolAdmissionForm(models.Model):
    _name = "school.admission.form"

    Student_Image = fields.Binary('Student Image')
    date_time = fields.Datetime('Date Time')
    Sibling_Standard = fields.Selection([('1st std', '1st std'), ('2nd std', '2nd std'),
                                         ('3th std', '3th std'), ('4th std', '4th std'),
                                         ('5th std', '5th std'), ('6th std', '6th std'),
                                         ('7th std', '7th std'), ('8th std', '8th std'),
                                         ('9th std', '9th std'), ('10th std', '10th std'),
                                         ('11th std', '11th std'), ('12th std', '12th std')], string="Standard")
    Subjects_Available = fields.Many2many('school.subjects.available', 'school_subject_rel', 'subject_id', 'school_id',
                                          string="Subject")
    Student_Name = fields.Char('Student Name')
    Last_Name = fields.Char('Last Name')
    DOB = fields.Date('DOB')
    age = fields.Integer("Age")
    Gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    Adress = fields.Char('Adress')
    Street1 = fields.Char('Street 1')
    Street2 = fields.Char('Street 2')
    City = fields.Char('City')
    State_id = fields.Many2one('res.country.state', 'State')
    Country_id = fields.Many2one('res.country', 'Country')
    Pincode = fields.Integer('PIN')
    Parent_Name = fields.Char('Parent Name')
    Last_Name = fields.Char('Last Name')
    Relation_To_Student = fields.Selection([('father', 'Father'), ('mother', 'Mother'),
                                            ('garden', 'Garden')], string="Relation To Student")
    Telno = fields.Integer('Tel.no.')
    Email = fields.Char('Email')
    Phnno = fields.Integer('Phn.no.')
    Siblings = fields.Selection([('yes', 'Yes'), ('no', 'No')], string="Siblings")
    Sibling_Name = fields.Char('Sibling Name')
    Last_Name = fields.Char('Last Name')
    Sibling_Relation = fields.Selection([('elder brother', 'Elder Brother'),
                                         ('elder sister', 'Elder Sister'),
                                         ('younger brother', 'Younger Brother'),
                                         ('younger sister', 'Younger Sister')], string="Sibling_Relation")
    Previous_School_id = fields.Many2one('school.school', 'Previous School')
    Marks_Obtained = fields.Float('Marks Obtained')
    Total_Marks = fields.Float('Total Marks')
    Percentage_Score = fields.Float(compute='_compute_percent', string='Percentage', store=True)
    Certificates = fields.Text('Certificates')
    Parent_Sign = fields.Binary('Parent Sign', required=True)
    Student_Sign = fields.Binary('Student Sign', required=True)
    state = fields.Selection([('draft', 'Draft'), ('inprogress', 'In-progress'), ('validate', 'Validate'), ('approved', 'Approved')],
                              default='draft', string='Status')

    def action_inprogress(self):
        if self.state == 'draft':
            self.state = 'inprogress'

    def action_validate(self):
        if self.state == 'inprogress':
            if self.Total_Marks >= 60:
                self.state = 'validate'
            else:
                raise ValidationError(_("Please enter the total marks above 60"))

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

    @api.depends('Marks_Obtained', 'Total_Marks')
    def _compute_percent(self):
        for record in self:
            if record.Marks_Obtained and record.Total_Marks:
                rere = record.Marks_Obtained / record.Total_Marks * 100
                record.update({
                    'Percentage_Score': rere
                })
