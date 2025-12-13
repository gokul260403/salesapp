import frappe
def push_sales_amount(doc):
    label=doc.name
    points=[doc.net_total]
    frappe.publish_realtime("sales_update",{'label':label,'points':points})