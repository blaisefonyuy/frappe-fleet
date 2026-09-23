import frappe
from frappe.utils import today, add_days, date_diff

def check_service_alerts():
    """Daily check for equipment with service due soon"""
    try:
        gs = frappe.get_doc("Garage Settings", "Garage Settings")
        alert_days = gs.service_alert_days or 7
    except Exception:
        alert_days = 7

    alert_date = add_days(today(), alert_days)

    equipment = frappe.get_all('Asset',
        filters={
            'custom_next_service_due': ['<=', alert_date],
            'custom_next_service_due': ['!=', ''],
        },
        fields=['name', 'asset_name', 'custom_next_service_due', 'custom_immatriculation']
    )

    if not equipment:
        return

    # Notify Garage Chief
    garage_chiefs = frappe.get_all('Has Role',
        filters={'role': 'Garage Chief'},
        fields=['parent']
    )

    for chief in garage_chiefs:
        if chief.parent == 'Administrator':
            continue
        try:
            frappe.sendmail(
                recipients=[chief.parent],
                subject=f"⚠️ Fleet Alert: {len(equipment)} equipment due for service",
                message=f"""
                <h3>Equipment Service Alert</h3>
                <p>The following equipment is due for service within {alert_days} days:</p>
                <table border="1" cellpadding="5">
                    <tr><th>Equipment</th><th>Plate</th><th>Next Service</th></tr>
                    {''.join(f"<tr><td>{e.asset_name}</td><td>{e.custom_immatriculation or ''}</td><td>{e.custom_next_service_due}</td></tr>" for e in equipment)}
                </table>
                <p>Please schedule maintenance accordingly.</p>
                """
            )
        except Exception:
            pass
