from odoo import api, fields, models


class Patient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _order = "id desc"

    name = fields.Char(string="Name", index=True)
    image = fields.Char(string="Patient Image")
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ['male', 'Male'],
        ['female', 'Female'],
        ['other', 'Other'],
    ], required=True, default="male")

    appointment_ids = fields.One2many(
        'hospital.appointment', 'patient_id', string="Appointments")
    doctor_ids = fields.Many2many(
        'hospital.doctor', 'doctor_patient_rel', string="Doctors")
    responsible_id = fields.Many2one('res.partner', string="Responsible")
    appointment_count = fields.Integer(
        string="Appointment Count", compute="_compute_appointment", )
