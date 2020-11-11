from odoo import models,fields,api

class  CourseCourse(models.Model):

	_name="course.course"
	_description="Course"

	name=fields.Char(string="Name")
	state=fields.Selection([('live','live'),('inactive','inactive')],string="state")
	code=fields.Char(string="Code")
	sem_ids=fields.One2many('course.semester.line','course_id',string="sem_ids")
	course_description=fields.Html(string="course description")
	active=fields.Boolean(string="active")


