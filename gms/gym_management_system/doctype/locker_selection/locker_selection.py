# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class LockerSelection(Document):
	def before_save(self):
		member_assigned_lockers=frappe.db.get_all('Locker Selection',fields=['name','locker_number'])
		#print('\n\n\n\n',member_assigned_lockers,'\n\n\n\n\n',self.locker_number,'\n\n\n\n\n\n\n')
		for members_using_locker in member_assigned_lockers:
			if self.locker_number == members_using_locker['locker_number']:
				frappe.throw("locker is being occupied")
		
