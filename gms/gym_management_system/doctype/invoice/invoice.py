# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Invoice(Document):
	def before_save(self):


		################################################### Code for Classes attend and Class costs
		all_bookings= frappe.db.get_all('Class Booking',fields=['member_id','cost'])
		member_id=self.member_id
		sum=0
		for bookings in all_bookings:
			if member_id==bookings['member_id']:
				sum+=10000		
		self.classes_attended = sum/10000
		self.total_expense_this_month=sum

		################################################### Code for locker fields

		locker_list=frappe.db.get_all('Locker Selection',fields=['member_id','cost','locker_number'])
		for lockers in locker_list:
			if lockers['member_id']==member_id:
				self.locker_cost = lockers['cost']
				self.locker_occupied = lockers['member_id']
