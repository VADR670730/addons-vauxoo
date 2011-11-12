# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#
#    Copyright (c) 2011 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    Info (info@vauxoo.com)
############################################################################
#    Coded by: isaac (isaac@vauxoo.com)
#    Coded by: moylop260 (moylop260@vauxoo.com)
############################################################################
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from report import report_sxw
import time
import pooler
from dateutil.relativedelta import relativedelta
import datetime


class invoice_report_pagos(report_sxw.rml_parse):
    def __init__(self, cr, uid, name, context):
            super(invoice_report_pagos, self).__init__(cr, uid, name, context=context)
            self.localcontext.update({
                'time': time,
                'get_payment': self._get_payment,
                'get_invoice_payment': self._get_invoice_payment,
                'get_line_payment': self._get_line_payment,
                'get_total_pago': self._get_total_pago,

            })

    def _get_total_pago(self):
        print 'el get_total_pago es --------------------------------',self.tot_pago
        return self.tot_pago


    def _get_line_payment(self,pay_id, inv_id):
        print 'dentro de gety_line pyment y el param es'
        subq="""
                select b.id
                    from account_voucher a
                        inner join account_voucher_line b
                            on a.id=b.voucher_id
                        inner join account_move_line c
                            on c.id=b.move_line_id
                        inner join account_invoice d
                            on d.move_id=c.move_id
                    where a.id=%s
                    and d.id=%s
                """%( pay_id, inv_id )
        self.cr.execute( subq )
        invoice_ids = [ inv_id[0] for inv_id in self.cr.fetchall() ]
        print 'los ids de las lineas voucher son son',invoice_ids
        pay_obj = self.pool.get('account.voucher.line')
        pay_brw= pay_obj.browse(self.cr, self.uid, invoice_ids)[0]
        print 'el retorno de Line paymente es',pay_brw
        print 'pay_brw.amount--------------es',pay_brw.amount
        #~ for tot in pay_brw:
        self.tot_pago += pay_brw.amount

        print '===================================================dentro del for de pay_brw amnount:',pay_brw.amount

        return str(pay_brw.amount)

    def _get_invoice_payment(self,pay_id):
        print 'dentro de gety_line pyment y el param es'
        subq="""
                select d.id
                    from account_voucher a
                        inner join account_voucher_line b
                            on a.id=b.voucher_id
                            and b.amount>0
                        inner join account_move_line c
                            on c.id=b.move_line_id
                        inner join account_invoice d
                            on d.move_id=c.move_id
                    where a.id=%s
                """%( pay_id )
        self.cr.execute( subq )
        invoice_ids = [ inv_id[0] for inv_id in self.cr.fetchall() ]
        print 'los ids de la factura son',invoice_ids
        inv_obj = self.pool.get('account.invoice')
        inv_brw= inv_obj.browse(self.cr, self.uid, invoice_ids)
        print 'el retorno de paymente es',inv_brw
        self.tot_pago=0
        return inv_brw


    def _get_payment(self, partner_id):
        print 'partner id es',partner_id
        vou_obj = self.pool.get('account.voucher')
        vou_ids = vou_obj.search(self.cr, self.uid, [('partner_id', '=', partner_id)] )
        vou_brw= vou_obj.browse(self.cr, self.uid, vou_ids)
        print 'los ids de los voucher son',vou_ids
        #~ print 'lo browse de invoice es',inv_brw.internal_number
        self.vou_brw=vou_brw
        print 'el vou_brw es',vou_brw
        self.tot_pago=0
        return vou_brw

report_sxw.report_sxw('report.invoice.report.pagos', 'res.partner','addons/invoice_report/report/payment_report2.rml', parser=invoice_report_pagos)

