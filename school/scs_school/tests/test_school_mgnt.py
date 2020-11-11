from odoo.tests import common


class TestSchoolSchool(common.TransactionCase):
    """Test Case for School."""

    def setUp(self):
        """Initialize School Test Cases."""
        super(TestSchoolSchool, self).setUp()
        print("\n yes :::::::In TESTING FILE::::::::", self)

    def test_create_school(self):
        """Test Case to Create School."""
        company_id = self.env.ref('base.main_company')
        print("\n company_id ::::::::::", company_id)

        new_school = self.env['school.school'].create({
            'name': 'Sports School',
            'medium': 'english',
        })
        print("\n new_school :::::::::::", new_school)
