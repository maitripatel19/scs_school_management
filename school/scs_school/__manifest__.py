{
    # Module Info.
    "name": "SCS School",
    "version": "13.0.1.0.0",
    "sequence": 1,
    "category": "School",
    "license": 'LGPL-3',
    "summary": """SCS School .""",
    "description": """SCS School .""",

    # Author
    "author": "Serpent Consulting Services Pvt. Ltd.",
    "website": "http://www.serpentcs.com",

    # Dependencies
    "depends": ['contacts'],

    # Data
    "data": [
        "security/ir.model.access.csv",
        "data/student_sequence_number.xml",
        "data/email_template_view.xml",
        "data/hobby_data_student.xml",
        "views/school_css.xml",
        "views/scs_school_view.xml",
        "views/scs_student_view.xml",
        "views/course.xml",
        "views/student_semester.xml",
        "views/hobby_student.xml",
        "report/student_info_report.xml",
        "report/report_view.xml",
        "wizard/wiz_student_sem_fees.xml",
    ],
        
    

    # Odoo App Store Specific
    # 'images': ['static/description/export_data_security_banner.gif'],

    # Technical
    "application": True,
    "installable": True,
    'auto_install': False,

}