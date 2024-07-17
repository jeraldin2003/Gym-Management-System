// Copyright (c) 2024, Jerald and contributors
// For license information, please see license.txt

frappe.query_reports["Attendance report"] = {
    "filters": [
        {
            "fieldname": "month",
            "label": __("Month"),
            "fieldtype": "Select",
            "options": [
                { "value": "1", "label": __("January") },
                { "value": "2", "label": __("February") },
                { "value": "3", "label": __("March") },
                { "value": "4", "label": __("April") },
                { "value": "5", "label": __("May") },
                { "value": "6", "label": __("June") },
                { "value": "7", "label": __("July") },
                { "value": "8", "label": __("August") },
                { "value": "9", "label": __("September") },
                { "value": "10", "label": __("October") },
                { "value": "11", "label": __("November") },
                { "value": "12", "label": __("December") }
            ],
            "default": (new Date()).getMonth() + 1
        }
    ],
    formatter: function(value, row, column) {
       

        //value = default_formatter(value, row, column);

    ///////////////////////////////////////////////////////////////////////////
        if (column.colIndex > 1) {
            if (value == "Present") {
                value = "<span style='color:green'>" + value + "</span>";
            } else if (value == "Absent") {
                value = "<span style='color:red'>" + value + "</span>";
            } 
        }   
    //////////////////////////////////////////////////////////////////////
        // Return in chAnged color
        return value;
    }

	"filters": [

	]
};
