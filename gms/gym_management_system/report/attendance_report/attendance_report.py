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

    data = frappe.db.sql("""
        SELECT
            attendance,
            mem_id,
            date
        FROM
            `tabMembers Daily Attendance`
        """, filters, as_dict=1)    

    print("\n\n\n\n\n\n\n\n", data_main)

    ###############DECLARING NEEDED THINGS#############
    today = frappe.utils.today()
    members = frappe.get_all('Member', fields=['name'])
    start_of_month = frappe.utils.data.get_first_day(today)
    end_of_month = frappe.utils.data.get_last_day(today)
    date = start_of_month
    ##############################################

    # Adding columns for each day in the month
    while date <= end_of_month:
        label = date.strftime("%Y-%m-%d")  # Format date as string for label
        fieldname = date.strftime("%Y-%m-%d")  # Fieldname can be same as label for simplicity
        columns.append({
            "label": label,
            "fieldname": fieldname,
            "fieldtype": "Data",
            "width": 100
        })
        date += timedelta(days=1)

    ################### CALCULATING THE ATTENDANCE #################
    member_attendance = frappe.get_all('Members Daily Attendance',
                                       fields=['mem_id', 'date', 'attendance'],
                                       filters={'date': ['between', [start_of_month, end_of_month]]})

    print("Member attendance records fetched:", member_attendance)  # Debugging line

    # Initialize dictionary to store attendance per member per date
    attendance_data = {member['name']: {col['fieldname']: 'Absent' for col in columns[1:]} for member in members}

    # Calculate attendance for each member on each date
    for attendance in member_attendance:
        mem_id = attendance['mem_id']
        date_str = attendance['date'].strftime("%Y-%m-%d")
        attendance_status = attendance['attendance']
        print(f"Processing attendance for {mem_id} on {date_str}: {attendance_status}")  # Debugging line
        if mem_id in attendance_data:
            attendance_data[mem_id][date_str] = attendance_status

    # Prepare the data for the report
    gate = [{'member_name': member['name'], **attendance_data[member['name']]} for member in members]

    print("Final gate data:", gate)  # Debugging line

    return columns, gate

























"""


	# Fetch all members
    
	members = frappe.get_all('Member', fields=['name'])

    # Fetch member attendance for the current month
    
	today = frappe.utils.today()
    
	start_of_month = frappe.utils.data.get_first_day(today)
    
	end_of_month = frappe.utils.data.get_last_day(today)

	

    
	member_attendance = frappe.get_all('Members Daily Attendance',
                                       fields=['mem_id', 'date'],
                                       filters={'date': ['between', [start_of_month, end_of_month]]})

    # Initialize dictionary to store days present per member
    
	days_present_count = {member['name']: 0 for member in members}

    # Calculate days present for each member
    
	for attendance in member_attendance:
		mem_id = attendance['mem_id']
		if mem_id in days_present_count:
			days_present_count[mem_id] += 1
	data = [{'member_name': member['name'], 'days_present': days_present_count.get(member['name'], 0)} for member in members]
	return columns, data
"""