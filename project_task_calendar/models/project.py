# -*- coding: utf-8 -*-
# Copyright (C) 2016 MultidadosTI (http://www.multidadosti.com.br)
# @author Michell Stuttgart <michellstut@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

from odoo import api, fields, models


class ProjectProject(models.Model):

    _inherit = 'project.project'

    partner_ids = fields.Many2many(comodel_name='res.partner',
                                   string='Related Partners')

    calendar_event_ids = fields.One2many(comodel_name="calendar.event",
                                         inverse_name="project_id",
                                         string="Calendar Events")

    bring_default_task_type = fields.Boolean(
        string="Get default stages",
        help="Add to this project, all stage defined like default")

    @api.model
    def create(self, vals):
        vals['partner_ids'] = [(4, vals['partner_id'])]
        res = super(ProjectProject, self).create(vals)

        if vals.get('bring_default_task_type'):
            task_types = self.env['project.task.type'].search([(
                'is_default', '=', 'True')])
            for rec in task_types:
                rec.project_ids = [(4, res.id)]

        return res

    @api.multi
    def write(self, values):
        # Add code here
        if 'partner_id' in values:
            values['partner_ids'] = [(4, values['partner_id'])]
        return super(ProjectProject, self).write(values)


class ProjectTaskType(models.Model):

    _inherit = 'project.task.type'

    is_default = fields.Boolean(string='Default',
                                help='Allows assignment of the current stage '
                                     'to new projects that will be created.')

    _sql_constraints = [('project_task_type_name_uniq', 'unique (name)',
                         'Already stage with same name!')]

