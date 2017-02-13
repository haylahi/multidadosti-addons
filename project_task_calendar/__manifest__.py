# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Aldo Soares <soares_aldo@hotmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    'name': 'Project Task in Calendar',
    'license': 'AGPL-3',
    'author': 'MultidadosTI',
    'version': '10.0.1.0.0',
    'website': 'www.multidadosti.com.br',
    'summary': """Custom module developed for visual improvement on project
               module and integration with calendar Support by MultidadosTI""",
    'category': 'Project',
    'contributors': [
        'Aldo Soares <soares_aldo@hotmail.com>',
        'Michell Stuttgart <michellstut@gmail.com>',
    ],
    'depends': [
        'project',
        'calendar',
    ],
    'data': [
        'views/view_calendar.xml',
        'views/view_project_project.xml',
        'views/view_project_task.xml',
    ],
    'installable': True,
}
