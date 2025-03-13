{
    'name': 'Fleet Custom',
    'version': '1.0',
    'summary': 'Customize Odoo Fleet Module',
    'category': 'Fleet',
    'author': 'Your Name',
    'depends': ['fleet'],  # Modul ini bergantung pada 'fleet'
    'data': [
        'security/ir.model.access.csv',
        'views/fleet_vehicle_view.xml',
        'views/fleet_vehicle_model_view.xml',
        'views/fleet_insurance_view.xml',
        'views/insurance_view.xml',
        'views/fleet_status_physical_view.xml',
        'views/fleet_status_unit.xml',
        'data/status_physical_data.xml',
        'data/status_unit_data.xml',
    ],
    'installable': True,
    'application': True,
}
