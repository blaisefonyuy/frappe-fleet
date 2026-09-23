app_name = "frappe_fleet"
app_title = "Frappe Fleet"
app_publisher = "Wirndzerem Blaise"
app_description = "Fleet & Garage Management for ERPNext"
app_email = "blaisefonyuy@gmail.com"
app_license = "mit"
app_version = "1.0.0"

required_apps = ["frappe", "erpnext"]

fixtures = [
    {"dt": "Custom Field", "filters": [["dt", "=", "Asset"]]},
    {"dt": "Role", "filters": [["name", "in", ["Fuel Agent","Purchase Officer","Garage Chief"]]]},
    {"dt": "Workflow State", "filters": [["name", "in", [
        "EER Draft","Pending Purchase Review","Pending DOO Approval",
        "EER Approved","EER Rejected","EER Paid"
    ]]]},
    {"dt": "Workflow", "filters": [["name","=","Equipment Expense Request Approval"]]},
    {"dt": "Print Format", "filters": [["name","in",["AMT Prebilling Minute"]]]},
]

after_install = "frappe_fleet.setup.install.after_install"

scheduler_events = {
    "daily": [
        "frappe_fleet.fleet_management.tasks.check_service_alerts",
    ]
}
