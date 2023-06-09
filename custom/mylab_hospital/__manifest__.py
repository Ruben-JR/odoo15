# -*- coding: utf-8 -*-
{
    "name": "MyLab Hospital",
    "summary": """Hospital management system""",
    "description": """Long description of module's purpose""",
    "sequence": -100,
    "author": "Ruben de Pina",
    "website": "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    "category": "Hospital",
    "version": "0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "mail"],
    # always loaded
    "data": [
        "security/ir.model.access.csv",
        "views/patient.xml",
        "views/appointment.xml",
        "views/menu.xml",
        # "views/templates.xml",
    ],
    # only loaded in demonstration mode
    "demo": [
        "demo/demo.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
    "license": "LGPL-3",
}
