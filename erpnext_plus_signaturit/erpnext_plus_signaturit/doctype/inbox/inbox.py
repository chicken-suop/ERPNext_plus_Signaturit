# -*- coding: utf-8 -*-
# Copyright (c) 2015, ratskin and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Inbox(Document):
	def on_update(self):
		from erpnext_plus_signaturit.tasks import inbox

		inbox() # Run inbox if form in doctype is edited
		