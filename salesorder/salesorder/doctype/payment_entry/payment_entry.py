# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class PaymentEntry(Document):
		def before_save(self):
			self.outstanding_amount=self.outstanding_amount-self.payable_amount
			amount=frappe.get_doc('Order',self.order)
			amount.outstanding_amount=self.outstanding_amount
			amount.save()
