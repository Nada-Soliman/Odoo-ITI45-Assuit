{
    'name':'ITI4',
    'summary':'ITI System',
    'author':'Nada-Soliman',
    'category':'Accounting',
    'website': "",
    'version':'0.1',
    'depends':['account','base','product'],
    'data':[
        'security/ir.model.access.csv',
        'security/iti_groups.xml',
        'views/base_menus.xml',
        'views/iti_student_views.xml',
        'views/iti_track_views.xml',
        'views/product_template_views.xml',
        'reports/iti_student_template.xml',
        'reports/iti_student_report.xml'
    ]
}