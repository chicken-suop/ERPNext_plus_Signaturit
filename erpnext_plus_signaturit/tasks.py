import frappe
from signaturit_sdk.signaturit_client import SignaturitClient

def inbox(*args):
	#====== download signatures ======#
	
	# Get data from signaturit using special ID:
	response = SignaturitClient("UtCJVghItkyqYAxwkgsQtsxrqzrndGBrcRnAvfppczXUmYhKZoEIgOTuPwWSFBaKELHLMsqjdVZIBqMsvGKHxD").get_signatures()
	tabInbox_values = []

	for pos, data in enumerate(response):
		# If that row is not already there then add it else don't:
		if frappe.db.sql("SELECT COUNT(1) FROM tabInbox WHERE name = '{}';".format(data["documents"][0]["id"]))[0][0] == 0:			
			for x in ["id", "status", "email", "created_at", "file"]: # Values we want to look for in signaturit data
				for key in data["documents"][0]:
					if key == x:
						if x == "file":
							tabInbox_values.append(data["documents"][0][key]["name"])
						else:
							tabInbox_values.append(data["documents"][0][key])
			# Insert into frappe database for inbox doctype a new row
			frappe.db.sql("INSERT INTO tabInbox (id, name, status, recipients, date, document_title) VALUES ({}, '{}', '{}', '{}', '{}', '{}');".format(pos+1, *tabInbox_values))
			#frappe.errprint
			tabInbox_values = []


	#tabInbox_values = ["tabInbox_name", "tabInbox_owner", "tabInbox_status", "tabInbox_recipients", "tabInbox_created_by", "tabInbox_date", "tabInbox_document_title"]
	#frappe.errprint('INSERT INTO tabInbox (name, owner, status, recipients, created_by, date, document_title) VALUES ({}, {}, {}, {}, {}, {}, {});'.format(*tabInbox_values))


	#====== download signed pdf ======#
	# document = client.download_signed_document("590648a5-f442-11e6-868f-0680f0041fef", "5924a612-f442-11e6-868f-0680f0041fef")
	# file = open("document.pdf", 'w')
	# file.write(document)
	# file.close()


	#====== get signatures ======#
	# client = SignaturitClient(self.signaturit_client)
	# file_path = ["/Users/elliotschep/frappe-bench/apps/erpnext_plus_signaturit/erpnext_plus_signaturit/files/doc.pdf"]
	# recipients =  [{
	# 			"name": self.recipient_name, 
	# 			"email": self.recipient
	# 			}]
	#
	# sign_params = {
	# 			"subject": self.subject, 
	# 			"body": self.body
	# 			}
	# # response = client.create_signature(file_path, recipients, {'delivery_type': 'url'})
	# # response = client.create_signature(file_path, recipients, sign_params)
	# response = [file_path[0], recipients[0], sign_params]