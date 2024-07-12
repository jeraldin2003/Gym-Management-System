# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document 


class Trainers(Document):
       def before_save(self):
        # frappe.throw('testing')
        print ('\n\n\n\n')
        trainers = frappe.get_all('Trainers', fields=['name','rating'])
        trainer_feedback = frappe.db.get_all('Trainer Feedback',fields=['trainer','rating'])
        print ("FEED BACK +======/n\n",trainer_feedback)
        print ("TRAINER====",trainers)
        
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
            print(a,trainer['name'])
            print('hellooooooooooooooooooooooooo\n\n\n\n\n\n\n')
            doc=trainer
            doc.rating = a
            
        
# def before_save(self):
# 		self.full_name = self.first_name + " " + self.last_name
		
		#self.full_name=f"{self.first_name} {self.last_name}"
				#not working 
