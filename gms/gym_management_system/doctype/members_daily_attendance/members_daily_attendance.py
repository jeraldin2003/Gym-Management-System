# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class MembersDailyAttendance(Document):
    pass
	#def before_save(self):
		#doc=frappe.get_all('Members Daily Attendance')
		#print(doc)
		#print("\n\n\n\n\n\n",self.name,'\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		#for attended in doc:	
		#	if self.name == doc:
		#		frappe.throw("try again")
