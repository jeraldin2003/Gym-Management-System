// Copyright (c) 2024, Jerald and contributors
// For license information, please see license.txt

frappe.query_reports["Report for customer fitness"] = {
    "filters": [
        {
            "fieldname": "member_id",
            "label": __("Member ID"),
            "fieldtype": "Link",
            "options": "Member",
            "reqd": 1
        }
    ]
};
