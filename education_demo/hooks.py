# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "education_demo"
app_title = "Education Demo"
app_publisher = "Frappe Technologies"
app_description = "Demo for ERP For Education"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "developers@frappe.io"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/education_demo/css/education_demo.css"
# app_include_js = "/assets/education_demo/js/education_demo.js"

# include js, css files in header of web template
# web_include_css = "/assets/education_demo/css/education_demo.css"
# web_include_js = "/assets/education_demo/js/education_demo.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "education_demo.install.before_install"
# after_install = "education_demo.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "education_demo.notifications.get_notification_config"

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
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"education_demo.tasks.all"
# 	],
# 	"daily": [
# 		"education_demo.tasks.daily"
# 	],
# 	"hourly": [
# 		"education_demo.tasks.hourly"
# 	],
# 	"weekly": [
# 		"education_demo.tasks.weekly"
# 	]
# 	"monthly": [
# 		"education_demo.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "education_demo.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "education_demo.event.get_events"
# }

