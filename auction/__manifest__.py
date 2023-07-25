{
    'name' : 'Auction',
    'version': '1.0',
    'author': "Aditya Dubey",

    'depends' : ['base', 'mail'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/auction_product.xml',
        'views/auction_bid.xml',
        'views/auction_product_type.xml',
        'views/auction_product_category.xml',
        'views/auction_menus.xml',
        'views/res_user_view.xml',
        'report/auction_product_report.xml',
        'report/auction_product_templates.xml'
    ]
}