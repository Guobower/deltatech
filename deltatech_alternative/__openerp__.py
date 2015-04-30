# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2008 Deltatech All Rights Reserved
#                    Dorin Hongu <dhongu(@)gmail(.)com       
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
{
    "name" : "Deltatech Products Alternative ",
    "version" : "1.0",
    "author" : "Dorin Hongu",
    "category" : "Generic Modules/Inventory Control",
    "depends" : ["product",'stock'],
    "init_xml" : [],
    "demo_xml" : [],
    "description": """
Features:    
 - A module that add alternative on the product form
 - New field in product: Dimensions, Shelf Life and Unit of Measure for Shelf Life    
 
""",
    "update_xml" : [
        "product_view.xml",
        'security/ir.model.access.csv',
    ],
    "active": False,
    "installable": True,
   
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: