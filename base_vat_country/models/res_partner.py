from odoo import models, api, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    vat_without_country = fields.Char(
        'TIN', help='Tax Identification Number. Fill it if the company is '
        'subjected to taxes. Used by the some of the legal statements. You no '
        'set the country prefix.',
        copy=False)
    country_code = fields.Char(
        help='Added the country code in partner, to complete the NIF.',
        related='country_id.code', size=2)

    @api.onchange('vat_without_country', 'country_code')
    def onchange_vat_wo_country(self):
        if self.vat_without_country:
            self.vat = (self.country_code or '  ') + self.vat_without_country
        else:
            self.vat = ''
