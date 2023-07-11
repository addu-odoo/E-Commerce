{
    'name' : 'Auction',
    'version': '1.0',
    'author': "Aditya Dubey",

    'depends' : ['base'],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/auction_product.xml',
        'views/auction_bid.xml',
        'views/auction_menus.xml'
    ]
}