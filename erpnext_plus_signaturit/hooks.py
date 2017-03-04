# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "erpnext_plus_signaturit"
app_title = "ERPNext_plus_Signaturit"
app_publisher = "ratskin"
app_description = "An integration of ERPNext and Signaturit"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "elliot.schep@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/erpnext_plus_signaturit/css/erpnext_plus_signaturit.css"
# app_include_js = "/assets/erpnext_plus_signaturit/js/erpnext_plus_signaturit.js"

# include js, css files in header of web template
# web_include_css = "/assets/erpnext_plus_signaturit/css/erpnext_plus_signaturit.css"
# web_include_js = "/assets/erpnext_plus_signaturit/js/erpnext_plus_signaturit.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "erpnext_plus_signaturit.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "erpnext_plus_signaturit.install.before_install"
# after_install = "erpnext_plus_signaturit.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "erpnext_plus_signaturit.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "erpnext_plus_signaturit.tasks.inbox"
# 	}
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
	"hourly": [
		"erpnext_plus_signaturit.tasks.inbox"
	]
}

# Testing
# -------

# before_tests = "erpnext_plus_signaturit.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "erpnext_plus_signaturit.event.get_events"
# }

