from odoo import models,fields,api


class SchoolSchool(models.Model):

    _name="school.school"
    _description = "School"

    name=fields.Char(string="Name of school")
    code=fields.Char(string="code")
    medium=fields.Selection([('hindi','Hindi'),
            ('english','English'),('both','Both'),('other','Other')],string="school medium")
    reg_fees=fields.Float(string="Registration fees")
    school_rating=fields.Selection([('0', '0'), ('1', '1'), ('2', '2'),
                                      ('3', '3'), ('4', '4'), ('5', '5')],
                                     string="Rating")
    student_id=fields.One2many("student.student","school_id",string="Students")
    
    def name_get(self):
        # print("\n self :::name_get::::::::", self)
        res = []
        for school in self:
            name = school.name
            # print("\n name :::::1::::::", name)
            if school.code:
                name = name + ' [ ' + school.code + ']'
            # print("\n name :::::1::::::", name)
            res.append((school.id, name))
        # print("\n res ::::::::::::::::", res)
        # Return : list of tupple [(record id, value),(record id, value)]
        return res