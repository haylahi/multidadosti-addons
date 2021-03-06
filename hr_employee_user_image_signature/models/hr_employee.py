# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import models, fields


class CustomUserHRSignature(models.Model):

    _inherit = 'hr.employee'

    image_signature = fields.Binary(string="Signature",
                                    help="This field holds the image used as "
                                         "signature for the employee, limited "
                                         "to 1024x1024px. It can be used in "
                                         "reports.")
