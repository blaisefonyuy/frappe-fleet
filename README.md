# 🚛 Frappe Fleet
### Fleet & Garage Management for ERPNext

Built by **AMT Cameroun SA** — a complete fleet management solution for logistics companies, oil & gas operators, and any organization managing heavy equipment in Cameroon and beyond.

---

## Features

| Feature | Description |
|---------|-------------|
| ⛽ Multi-Tank Fuel Management | Track Diesel, Super & Kerosene tanks with live levels |
| 🔧 Maintenance Log | Service history with parts tracking & auto alerts |
| 💰 Expense Request Workflow | Purchase Officer → Director of Operations approval |
| 📋 Monthly Prebilling | Auto-generate Prebilling Minute PDF per client |
| 📊 Fleet Dashboard | Live fuel levels, services due, pending requests |
| 📈 Profitability Analysis | Revenue vs cost per equipment over time |
| 🚗 Equipment Master | 20+ fleet tracking fields on ERPNext Asset |

## Installation

```bash
bench get-app git@github.com:blaisefonyuy/frappe-fleet.git
bench --site your-site.com install-app frappe_fleet
bench --site your-site.com migrate
```

## Requirements
- ERPNext 15+
- Frappe 15+

## Roles Created on Install
- **Fuel Agent** — fuel dispensing only
- **Purchase Officer** — expense request management
- **Garage Chief** — full fleet management & dashboard

## License
MIT — AMT Cameroun SA 2026
