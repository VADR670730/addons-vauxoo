#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) OpenERP Venezuela (<http://openerp.com.ve>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Jorge Naranajo <jorge_nr@vauxoo.com>
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

{
    "name" : "Account Move Validate Wizard",
    "version" : "0.1",
    "author" : "Vauxoo",
    "category" : "Generic Modules",
    "website": "http://www.vauxoo.com",
    "description": '''
    When you install this wizard. You can validate multi polizas.
''',
    "depends" : [
                "account",
                ],
    "demo_xml" : [], 
    "update_xml" : [
        'view/wizard.xml',
    ],
    "active": False,
    "installable": True
}
