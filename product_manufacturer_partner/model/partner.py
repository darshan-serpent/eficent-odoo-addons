# -*- coding: utf-8 -*-
# © 2015-17 Eficent Business and IT Consulting Services S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from openerp import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    manufacturer = fields.Boolean('Manufacturer')
