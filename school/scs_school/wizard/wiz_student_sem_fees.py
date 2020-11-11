from odoo import models, fields

class WizStudentSemFees(models.TransientModel):


    _name = 'wiz.student.sem.fees'
    _description = "Wizard Student Sem Fees"

    student_id=fields.Many2one("student.student",string="Student")
    semester_id=fields.Many2one("student.semester",string="Sem")
    amount=fields.Float(string="Amount")
    
   
        # for wiz in self:
          # print("::::::11:",self)
    def student_sem_fees(self):
        print(":::::::;1:::::;",self)
        for wiz in self:
            print("::::::1:::::::::",wiz.student_id.name)
            print(":::::;2:::::::",wiz.semester_id)
            print("::::3::::::",wiz.amount)
            if wiz.semester_id and wiz.amount:
                wiz.semester_id.write({'amount_paid': wiz.amount})
