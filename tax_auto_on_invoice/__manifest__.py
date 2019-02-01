# -*- coding: utf-8 -*-
# Copyright 2018 Ahmed Foudhaili <http://www.corail-technologie.com>

# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
{
    'name': "Tax Auto on invoice",

    'summary': """
        Permet la declaration d'une taxe à ajouter automatiquement sur la facture (pas sur le produit)
        Exemple : Timbre Ficale""",

    'description': """
        Permet la declaration d'une tax à ajouter automatiquement sur la facture (pas sur le produit)
        Exemple : Timbre Ficale
    """,

    "author": "Corail Technologie",
    "website": "http://www.corail-technologie.com",
    
    'category': 'Accounting',
    'version': '1.0',
    'depends': ['base','account'],
    'data': [
        'views/views.xml',
    ],
  
}