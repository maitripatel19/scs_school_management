from odoo import models,fields

class HobbyStudent(models.Model):

	_name="hobby.student"
	_description ="Hobby"

	name=fields.Char(string="Hobby name")