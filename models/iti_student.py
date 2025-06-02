from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class ITIStudent(models.Model):
    _name = "iti.student"

    # _rec_name = "age"
    name = fields.Char("Name")
    age = fields.Integer(string="age", store=True, compute="compute_age")
    graduate_age = fields.Integer( store=True, compute="compute_age")
    salary = fields.Float()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()


    is_working = fields.Boolean("")
    cv = fields.Html()
    levels = fields.Selection([('level1','Level1'),('level2','Level2'),('level3','Level3')])



    track_id = fields.Many2one("iti.track")

    track_capacity = fields.Integer(related="track_id.capacity")
    is_opened = fields.Boolean(related="track_id.is_opened")

    level_logs = fields.One2many('iti.student.log','student_id')

    roll_id = fields.Char()

    _sql_constraints = [('unique_roll_id','UNIQUE(roll_id)',"Roll Id can't be duplicate for each student")]

    @api.onchange('is_working')
    def change_work_state(self):
        print("in function")
        self.salary  = 50000

    def approve_action(self):
        print("in button action")
        self.salary = 60000
        self.levels = "level3"

    def create_patient_log(self):
        vals = {'description': "State changed to %s" % (self.state), 'patient_id': self.id}

        self.env['hms.patient.log'].create(vals)
    def create_level_log(self):
        vals = {

            'description': "Level changed to %s" %(self.levels),
            'student_id': self.id
         }
        self.env['iti.student.log'].create(vals)

    @api.constrains('age')
    def check_age(self):
        if self.age < 0:
            raise ValidationError("Age can't be negative number")
        elif self.age == 0:
            raise ValidationError("Age can't be zero")

    @api.constrains('is_working','salary')
    def check_salary(self):
        if self.is_working == True:
            if self.salary < 10000:
                raise ValidationError("Salary can't be less than 10000")

    @api.depends('age', 'graduate_age', 'birth_date')
    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
                rec.graduate_age = rec.age + 5
                print(f"Computed age for {rec.name}: {rec.age}")
            else:
                rec.age = 0
                rec.graduate_age = rec.age + 5



