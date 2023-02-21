from odoo import api, fields, models, _


class Appointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"

    name = fields.Char(
        string='Name', required=True, copy=False, readonly=True, default=lambda self: _('New'))

    patient_id = fields.Many2one(
        'hospital.patient', string="Patient", required=True)
    doctor_id = fields.Many2one(
        'hospital.doctor', string="Doctor", required=True)
    state = fields.Selection([('draft', 'Draft'), ('confirm', 'Confirmed'),
                              ('done', 'Done'), ('cancel', 'Cancelled')], default='draft',
                             string="Status",)
    date_appointment = fields.Date(string="Date")
    date_checkup = fields.Datetime(string="Check Up Time")
    prescription = fields.Text(string="Prescription")
