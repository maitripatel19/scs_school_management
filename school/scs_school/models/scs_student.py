from datetime import datetime
from odoo import models,fields,api,_
from datetime import datetime
from odoo.exceptions import ValidationError

class StudentStudent(models.Model):

    _name="student.student"
    _description = "Student"

    name=fields.Char(string="Name")
    image=fields.Binary(string="img")
    id_card=fields.Char(string=" ID card")
    roll_number=fields.Char(string=" roll no")
    birth_date=fields.Date(string=" birthdate")
    school_id=fields.Many2one("school.school",string="School")
    school_code=fields.Char(related="school_id.code", string="School code")
    age=fields.Float(compute="_compute_student_age" ,string="Age")
    state=fields.Selection([('new','new'),('confirmed','confirmed'),('cancel','cancel'),('pending','pending')],default="new",string="states")
    email = fields.Char(string="Email")
    course_id=fields.Many2one('course.course',string="Course")
    sem_ids=fields.One2many("student.semester",'student_id',string='Semesters')
    hobby_ids=fields.Many2many("hobby.student","student_hobby_rel","student_id","hobby_id",string="hobby")
    total_fees=fields.Float(compute="_compute_total_fees", string="Total Fees")
    total_paid_fees=fields.Float(compute="_compute_total_paid_fees", string="Total paid fees")
    wiz_ids=fields.One2many("wiz.student.sem.fees","student_id",string="wizIds")
    wiz_sems=fields.One2many("wiz.student.sem.fees","semester_id",string="wizSem")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('other', 'Other')], string="Gender")

    @api.depends('sem_ids')
    def _compute_total_fees(self):
        print(":::::::::",self)
        for student in self:
            print("::::student:::::",student)
           
            print("::::student.sem_ids:::::",student.sem_ids)
            tot_sem_fees = 0.0
            for sem in student.sem_ids:
                print("::::sem:::::",sem)
                print("::::sem.sem_fees:::::",sem.sem_fees)
                tot_sem_fees = tot_sem_fees + sem.sem_fees
            print("::::tot_sem_fees:::::",tot_sem_fees)
            student.total_fees = tot_sem_fees

    @api.depends('sem_ids')
    def _compute_total_paid_fees(self):
        print(":::::",self)
        for student in self:
            print(":::::::::student1111:::",student)
            print("::::;sem ids111:",student.sem_ids)
            total_fees=0.0
            for sem in student.sem_ids:
                print(":;:sem19:",sem)
                print(":;;;sem amount:::;",sem.amount_paid)
                total_fees=total_fees+sem.amount_paid
            print(":::::;total_fees::",total_fees)
            student.total_paid_fees=total_fees

            

    @api.depends('birth_date')
    def _compute_student_age(self):
        current_date=datetime.now().date()
        for student in self:
            diff_age=0.0
            if student.birth_date:
                diff_age=current_date.year-student.birth_date.year
            student.age=diff_age

    def action_new(self):
        for student in self:
            student.state= 'new'

    # def action_confirmed(self):
    #     for student in self:
    #         student.id_card=self.env['ir.sequence'].\
    #             next_by_code('student.student')
    #         student.state = 'confirmed'
    #     prin(":::::::::::")
    def action_confirm(self):
        """Method to move student in confirmed state."""
        print("action_confirm Call :::::::1::::::")
        template_id = \
            self.env.ref("scs_school.student_confirmation_mail_template")
        print("\n template_id ::::::::", template_id)
        for student in self:
            print("\n student:::", student)
            if student.email and template_id:
                template_id.send_mail(student.id, force_send=True)
            student.state = 'confirmed'
            print("action_confirm Call :::::::3::::::")


    def action_cancel(self):
         for student in self:
            student.state='cancel'

    @api.onchange('course_id')
    def _onchange_course_id(self):
        # for student in self:
            # student.sem_id=''
            # if student.course_id and student.course_id.sem_id:
            #     student.sem_id=student.course_id.sem_id
            print("::::::::::;",self)
            print("::::::::::::",self.course_id)
            print(":::::::::::::::::",self.course_id.sem_ids)
            sem_vals = []

            if self.course_id and self.course_id.sem_ids:
                self.sem_ids = [(6, 0, [])]
                for sem_l in self.course_id.sem_ids:
                    sem_vals.append((0, 0, {
                        'sem_id': sem_l.id,
                        'sem_fees': sem_l.sem_fees
                    }))
            self.sem_ids = sem_vals
            # (0, 0, { values })

    @api.constrains('name')
    def _check_birth_date(self):
        current_date = datetime.now().date()
        print(":::::::::::::::",self)
        for student in self:
                # if current_date < student.birth_date:
                #     raise ValidationError("birthdate must be less than current date.")
            print("::::birthdate:::;",student.birth_date)
            if current_date < student.birth_date:
                raise ValidationError("birthdate must be less than current date.")
