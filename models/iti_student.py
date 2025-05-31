from odoo import models, fields, api


class ITIStudent(models.Model):
    _name = "iti.student"

    # _rec_name = "age"
    name = fields.Char("Name")
    age = fields.Integer(string="age")
    salary = fields.Float()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()

    is_working = fields.Boolean("")
    cv = fields.Html()

    track_id = fields.Many2one("iti.track")

    track_capacity = fields.Integer(related="track_id.capacity")
    is_opened = fields.Boolean(related="track_id.is_opened")

    @api.onchange('is_working')
    def change_work_state(self):
        print("in function")
        self.salary  = 50000

        return {
            'warning': {
                'title': ('state changed'),
                'message': 'Working State is changed to %s' %(self.is_working)
            }
        }

    def approve_action(self):
        print("in button action")
        self.salary = 60000