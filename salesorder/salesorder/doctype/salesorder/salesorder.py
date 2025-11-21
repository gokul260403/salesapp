# Copyright (c) 2025, gokul and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.utils import today
from frappe.utils import nowdate, formatdate

class Salesorder(Document):
	def before_save(self):
		# self.date=today()
		self.date=nowdate()
  
@frappe.whitelist()
def daily_sales_order_summary():
	today = nowdate()

	total_orders = frappe.db.count(
		"Salesorder",
		filters={"date": today}
	)
	message = f" Total Sales Orders created on {formatdate(today)}: {total_orders}"
	frappe.get_doc({
		"doctype": "Notification Log",
		"subject": "Daily Sales Order Summary",
		"email_content": message,
		"for_user": "Administrator",
		"type": "Alert"
	}).insert(ignore_permissions=True)


	frappe.log_error(message, "Daily Sales Order Summary")

		# frappe.publish_realtime(
        #     message=message,
        #     user="Administrator"
		# )
  
		# frappe.get_doc({
		# 	"doctype": "Notification Log",
		# 	"subject": "Daily Sales Summary",
		# 	"document_type": "Salesorder",
		# 	"document_name": self.name,
		# 	"from_user": frappe.session.user,
		# 	"for_user": "Administrator",
		# 	"email_content": message
		# }).insert(ignore_permissions=True)	



		# recipients = frappe.db.get_all(
		# 	"Has Role",
		# 	filters={"role": ["in", ["Sales User", "Sales Manager"]]},
		# 	fields=["parent"]
		# )
		# user_list = [r.parent for r in recipients]


		# for user in user_list:
		# 	frappe.publish_realtime(
		# 		event="msgprint",
		# 		message=message,
		# 		user=user
		# 	)
        

		# frappe.log_error(message, "Daily Sales Order Summary")
  
  
   




@frappe.whitelist()
def save(item):
	total=0
	for i in item:
		total+=i.price
	return float(total)