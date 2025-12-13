// Copyright (c) 2025, gokul and contributors
// For license information, please see license.txt

frappe.query_reports["Sales Analytics Report"] = {
	"filters": [
		{
            'fieldname': 'name',
            'label': "Order Id",
            'fieldtype':'Link',
			'options': 'Order',
        }

	]
};
