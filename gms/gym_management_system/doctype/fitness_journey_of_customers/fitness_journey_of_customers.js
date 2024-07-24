// Copyright (c) 2024, Jerald and contributors
// For license information, please see license.txt

// frappe.ui.form.on("fitness journey of customers", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('fitness journey of customers', {
    weight: function(frm) {
        if (frm.doc.weight) {
            const poundsPerKg = 2.20462;
            frm.set_value('weight_in_lbs', (frm.doc.weight * poundsPerKg).toFixed(2));
        }
    }
});

