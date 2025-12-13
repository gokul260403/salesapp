# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns=get_columns()
    data=get_data(filters)
    chart=get_chart(data)
    return columns, data , None,chart

def get_columns():
    columns=[
          {
            'fieldname': 'name',
            'label': "Order Id",
            'fieldtype': 'Link',
            'options': 'Order',
            'width': 120
        },
		{
            'fieldname': 'customer_name',
            'label': "Customer Name",
            'fieldtype': 'Link',
            'options': 'Customer',
            'width': 120
        },
        {
            'fieldname': 'item',
            'label': "Item",
            'fieldtype':'Link',
            'options': 'Item List',
            'width': 120
        },
        {
            'fieldname': 'rate',
            'label': "Rate",
            'fieldtype':'Link',
            'options': 'Item List',
            'width': 120
        },
        {
            'fieldname': 'quantity',
            'label': "Quantity",
            'fieldtype':'Data',
            'width': 120
        },
        {
            'fieldname': 'price',
            'label': "Price",
            'fieldtype':'currency',
            'width': 120
        },
        {
            'fieldname': 'tax_amount',
            'label': "Tax Amount",
            'fieldtype': 'Currency',
            'width': 120
        },
        {
            'fieldname': 'net_total',
            'label': "Net Total",
            'fieldtype': 'Currency',
            'width': 120
        },
        {
            'fieldname': 'outstanding_amount',
            'label': "Outstanding Amount",
            'fieldtype': 'Currency',
            'width': 120
        },
	]
	
    
    return columns

def get_data(filters=None):
	conditions={}
	if filters.get("name"):
		conditions["name"] = filters.get("name")
		
	Orders=frappe.get_all("Order",filters=conditions,fields=
		["name","customer_name","tax_amount","net_total","outstanding_amount","payment_status"]
	)
	data=[]

	for order in Orders:
		Items=frappe.get_all("Items",filters={"parent":order.name},fields=["item","rate","quantity","price"])

		for item in Items:
			data.append({**order,**item})

	return data 


def get_chart(data):
    type_count = {"Pending": 0, "Completed": 0}

    for entry in data:
        status = entry.get("payment_status")
         

        if status == "Pending":
            type_count["Pending"] += 1
           
        elif status == "Completed":
            type_count["Completed"] += 1
             

    chart = {
        "data": {
            "labels": ["Pending", "Completed"],
            "datasets": [
                {
                    "name": "Payment",
                    "values": [type_count["Pending"], type_count["Completed"]],
                }
            ],
        },
        "type": "donut",
        "height": 120,
    }

    return chart


 