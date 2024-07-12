# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document 

class Trainers(Document):
       def before_save(self):

        latest_doc= frappe.get_last_doc('Trainer Feedback')
        doc_data = frappe.db.get_value('Trainer Feedback',latest_doc,'trainer')
        #print("\n\n\n",doc_data,"\n\n\n\n\n")
      
        trainers = frappe.get_all('Trainers', fields=['name','rating'])
        #print("\n\n\n\n\n\n",trainers )
        trainer_feedback = frappe.db.get_all('Trainer Feedback',fields=['trainer','rating'])
        trainer=doc_data
        for trainer in trainers:
            c=0
            a=0
            x=0
            for feedback in trainer_feedback:
                if feedback['trainer'] == trainer['name']:
                    y=feedback['rating']
                    x=x+y
                    c=c+1
            a=x/c
            b=trainer['name']
            print("\n\n\n\n",b,"\n\n\n\n\n")
            print(a,trainer['name'])
            #print('hellooooooooooooooooooooooooo\n\n\n\n\n\n\n')
            #print(trainer,'\n\n\n\n\n')

            frappe.db.set_value('Trainers','Ron-Loads-13','rating','100')
            frappe.db.commit()
            


# def before_save(self):
# 		self.full_name = self.first_name + " " + self.last_name
		
		#self.full_name=f"{self.first_name} {self.last_name}"
				#not working 
