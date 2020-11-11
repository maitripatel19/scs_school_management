from odoo import models,fields,api

class StudentSemester(models.Model):
	_name="student.semester"
	_description="student.semester"
	_rec_name = "sem_id"
   

	sem_id=fields.Many2one('course.semester.line',string="semester")
	sem_fees=fields.Float(string="Fees")
	amount_paid=fields.Float(string="Amount paid")
	remaining_amt=fields.Float(compute="_compute_remaining_amt", string="Remaining fees", store=True)
	student_id=fields.Many2one('student.student',string="student")


	@api.depends('amount_paid','sem_fees')
	def _compute_remaining_amt(self):
		print ("\n self ::::::::::::::", self)
		for stu_sem in self:
			print(':::stu_sem:::',stu_sem)
			print(':::stu_sem.sem_fees:::',stu_sem.sem_fees)
			print(':::stu_sem.amount_paid:::',stu_sem.amount_paid)
			# stu_sem.remaining_amt=1
				# student.semester.remaining_amt=len(sem_obj)
			# remaining_amt=sem_fees.stu_sem-amount_paid.stu_sem
			# print("::::::::::::",remaining_amt)
			# print("::::::::",sem_fees)
			remaining_amt = stu_sem.sem_fees- stu_sem.amount_paid
			stu_sem.remaining_amt = remaining_amt
			# stu_sem.write({})
			print("::remaining_amt:::",remaining_amt)