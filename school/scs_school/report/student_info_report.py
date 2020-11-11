from odoo import api,models

class StudentInfoReport(models.AbstractModel):
    """School Information Report AbstractModel."""

    _name = 'report.scs_school.student_info_report'
    _description = 'Student Information Report'

    # def _get_students(self, school=False):
    #     student_lst = []
    #     if student and school.student_ids:
    #         print ("\n student::::::::::::", student)
    #         student_lst = school.student_ids
    #     return student_lst

    @api.model
    def _get_report_values(self, docids, data=None):
        """Method to render the School Information Report template."""
        print("\n docids, data ::::::::::", docids, data)
        schools = []
        if docids:
            schools = self.env['student.student'].browse(docids)
        docargs = {
            'docids': docids,
            'doc_model': 'student.student',
            'docs': schools,
            'data': data,
            # 'get_students': self._get_students
        }
        return docargs