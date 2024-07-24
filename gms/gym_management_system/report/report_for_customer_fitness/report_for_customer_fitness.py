# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)

    # Calculate totals and averages
    total_weight = sum(d['weight'] for d in data)
    total_calories = sum(d['calories_consumed'] for d in data)
    count = len(data)
    avg_weight = total_weight / count if count > 0 else 0
    avg_calories = total_calories / count if count > 0 else 0

    # Append totals and averages to the data
    data.append({
        'date': 'Total',
        'weight': total_weight,
        'calories_consumed': total_calories
    })
    data.append({
        'date': 'Average',
        'weight': avg_weight,
        'calories_consumed': avg_calories
    })

    return columns, data

def get_columns():
    return [
        {"label": _("Date"), "fieldname": "date", "fieldtype": "Data", "width": 120},
        {"label": _("Weight (kg)"), "fieldname": "weight", "fieldtype": "Float", "width": 120},
        {"label": _("Calories Consumed"), "fieldname": "calories_consumed", "fieldtype": "Float", "width": 150},
    ]

def get_data(filters):
    conditions = ""
    if filters.get("member_id"):
        conditions += " and member_id=%(member_id)s"
    
    data = frappe.db.sql("""
        select
            date, weight, calories_consumed
        from
            `tabfitness journey of customers`
        where
            1=1 {conditions}
        order by
            date desc
    """.format(conditions=conditions), filters, as_dict=1)

    return data





















#def execute(filters=None):
#	columns = [{
 #           "label": "Date",
#            "fieldname": "date",
 #           "fieldtype": "date",
 #           "width": 150
 #       }]
#	data = frappe.db.sql("""
 #       SELECT 
  #          date
  #      FROM
  #          `tabfitness journey of customers`
   #     """, filters, as_dict=1)
#	return columns, data

