from odoo import models,fields,api

class CourseSemesterLine(models.Model):

	_name="course.semester.line"
	_description = "course.semester.line"

	name=fields.Char(string="Name")
	code=fields.Char(string="Code")
	sem_fees=fields.Float(string="Semfess")
	course_id=fields.Many2one("CourseCourse",string="course")