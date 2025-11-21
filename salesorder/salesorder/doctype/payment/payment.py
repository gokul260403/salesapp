# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Payment(Document):
	# def before_save(self):
	# 	self.outstanding_amount=self.outstanding_amount-self.payable_amount
	# 	amount=frappe.get_doc('Salesorder',self.sales_order)
	# 	amount.outstanding_amount=self.outstanding_amount
	# 	amount.save()
    pass