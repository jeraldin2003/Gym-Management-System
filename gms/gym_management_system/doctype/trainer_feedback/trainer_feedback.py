# Copyright (c) 2024, Jerald and contributors
# For license information, please see license.txt
# 

import frappe
from frappe.model.document import Document

class TrainerFeedback(Document):
    #code for finding average of trainer rating 
    def before_save(self):
        ###coding logic for calculating ratinglatest_doc= frappe.get_last_doc('Trainer Feedback')

        #getting latest entry
        latest_doc= frappe.get_last_doc('Trainer Feedback')
        print('\n\n\n\n')
        print (self.rating)

        #getting latest entry values
        trainer = frappe.db.get_value('Trainer Feedback',latest_doc,'trainer')

        #getting all the trainers data
        trainers = frappe.get_all('Trainers', fields=['name','rating'])


        #getting all the feedbacks
        trainer_feedback = frappe.db.get_all('Trainer Feedback',fields=['trainer','rating'])

        #loop to iterate each trainer once
        for trainer in trainers:
            c=0
            a=0
            x=0
            #loop to iterate each feedback
            for feedback in trainer_feedback:
                #selecting the feedbacks that belong to a specific trainer from trainer_feedback
                if feedback['trainer'] == trainer['name']:
                    y=feedback['rating']
                    x=x+y
                    c=c+1   
            a=x/c
            b=trainer['name']

        ###use frappe.set_value to insert the value to particular field 
    

            frappe.db.set_value('Trainers',b,'rating',a)


    #code for feedback range to be between 0 and 5
    def before_submit(self):

        #getting latest doc after save 
        lat=frappe.get_last_doc('Trainer Feedback')

        #getting values of the doc 
        lats=frappe.db.get_value('Trainer Feedback', lat, 'rating')
        
        #condition 
        if lats>5 or lats < 0:
            frappe.throw("Enter in the range of 0-5")
















        #print(dac.rating,'\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
        #frappe.throw("HELLO")
        #if dac.rating>5:   
            #frappe.throw("doc\n\n\n\n\n\n\n")


    
##############################################################------------------------------------------------------------
    #def before_save(self):
     #   latest_doc = frappe.get_last_doc('Trainer Feedback')
      #  print(latest_doc,"\n\n\n\n")

#def get_latest_feedback():
 #   return frappe.get_last_doc('Trainer Feedback')




        