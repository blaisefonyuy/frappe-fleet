import frappe

def after_install():
    """Run after app installation"""
    create_roles()
    create_garage_settings()
    create_asset_category()
    print("✅ Frappe Fleet installed successfully")

def after_migrate():
    """Run after every migrate"""
    pass

def create_roles():
    for role_name in ['Fuel Agent', 'Purchase Officer', 'Garage Chief']:
        if not frappe.db.exists('Role', role_name):
            frappe.get_doc({
                'doctype': 'Role',
                'role_name': role_name,
                'desk_access': 1
            }).insert(ignore_permissions=True)
            print(f"Created role: {role_name}")

def create_garage_settings():
    if frappe.db.exists('DocType', 'Garage Settings'):
        if not frappe.db.exists('Garage Settings', 'Garage Settings'):
            gs = frappe.new_doc('Garage Settings')
            gs.internal_fuel_price = 850
            gs.diesel_price = 850
            gs.super_price = 900
            gs.kerosene_price = 800
            gs.diesel_tank_capacity = 10000
            gs.super_tank_capacity = 2000
            gs.kerosene_tank_capacity = 1000
            gs.garage_location = 'Main Garage'
            gs.flags.ignore_permissions = True
            gs.insert()
            print("Created: Garage Settings")

def create_asset_category():
    if not frappe.db.exists('Asset Category', 'Fleet Equipment'):
        company = frappe.db.get_single_value('Global Defaults', 'default_company')
        if not company:
            return
        ac = frappe.new_doc('Asset Category')
        ac.asset_category_name = 'Fleet Equipment'
        ac.enable_cwip_accounting = 0
        fixed = frappe.get_all('Account',
            filters={'company': company, 'account_type': 'Fixed Asset'},
            fields=['name'], limit=1)
        depr = frappe.get_all('Account',
            filters={'company': company, 'account_type': 'Depreciation'},
            fields=['name'], limit=1)
        accum = frappe.get_all('Account',
            filters={'company': company, 'account_type': 'Accumulated Depreciation'},
            fields=['name'], limit=1)
        if fixed:
            ac.append('accounts', {
                'company_name': company,
                'fixed_asset_account': fixed[0].name,
                'accumulated_depreciation_account': accum[0].name if accum else '',
                'depreciation_expense_account': depr[0].name if depr else '',
            })
        ac.flags.ignore_permissions = True
        ac.flags.ignore_mandatory = True
        ac.insert()
        print("Created: Fleet Equipment asset category")
