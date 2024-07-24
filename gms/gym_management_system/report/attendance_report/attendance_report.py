# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from datetime import datetime, timedelta

def execute(filters=None):
    columns = [
        {
            "label": "User Name",
            "fieldname": "member_name",
            "fieldtype": "Data",
            "width": 150
        }
    ]

    data_main = frappe.db.sql("""
        SELECT 
            name
        FROM
            `tabMember`
        """, filters, as_dict=1)

    ############### DECLARING NEEDED THINGS #############
    today = frappe.utils.today()
    members = frappe.get_all('Member', fields=['name'])

    # Determine the start and end dates of the selected month
    if filters and 'month' in filters:
        month = int(filters['month'])
        year = datetime.today().year
        start_of_month = datetime(year, month, 1).date()
        end_of_month = frappe.utils.data.get_last_day(start_of_month)
    else:
        start_of_month = frappe.utils.data.get_first_day(today)
        end_of_month = frappe.utils.data.get_last_day(today)

    # Convert dates to datetime for comparison
    start_of_month_dt = datetime.combine(start_of_month, datetime.min.time())
    end_of_month_dt = datetime.combine(end_of_month, datetime.max.time())
    
    date = start_of_month
    ##############################################

    # Adding columns for each day in the selected month
    while date <= end_of_month:
        label = date.strftime("%Y-%m-%d") 
        month_str = date.strftime("%m")  # Store only the month in a variable (for debugging purpose)
        #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', month_str)
        fieldname = date.strftime("%Y-%m-%d") # Fieldname can be same as label for simplicity
        columns.append({
            "label": label,
            "fieldname": fieldname,
            "fieldtype": "Date",
            "width": 200
        })
        date += timedelta(days=1)

    ################### CALCULATING THE ATTENDANCE #################
    member_attendance = frappe.get_all('Member Daily Attendance',
                                       fields=['mem_id', 'date', 'attendance'],
                                       filters={'date': ['between', [start_of_month_dt, end_of_month_dt]]})

    # Initialize dictionary to store attendance per member per date
    attendance_data = {member['name']: {col['fieldname']: 'Absent' for col in columns[1:]} for member in members}

    # Calculate attendance for each member on each date
    for attendance in member_attendance:
        mem_id = attendance['mem_id']
        date_str = attendance['date'].strftime("%Y-%m-%d")
        attendance_status = attendance['attendance']
        if mem_id in attendance_data:
            attendance_data[mem_id][date_str] = attendance_status

    # Prepare the data for the report
    gate = [{'member_name': member['name'], **attendance_data[member['name']]} for member in members]  
    #print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',frappe.db.get_all('Member Daily Attendance'))
    return columns, gate