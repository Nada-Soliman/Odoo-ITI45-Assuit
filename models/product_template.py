from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class ProductTemplateInherit(models.Model):
    _inherit = "product.template"

    barcode2 =  fields.Char("Barcode 2")






