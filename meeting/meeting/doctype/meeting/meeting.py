# -*- coding: utf-8 -*-
# Copyright (c) 2021, Fusi and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
# import frappe
from frappe.model.document import Document

class Meeting(Document):
	# pass
	def validate(self):
		"""Set missing names and warn if duplicate"""
		# print("test")
		# for attendee in self.get("attendees"):
		found = []
		for attendee in self.attendees:
			if not attendee.full_name:
				# user = frappe.get_doc("User", attendee.attendee)
				# # concatenates by space if it has value
				# attendee.full_name = " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
				attendee.full_name = get_full_name(attendee.attendee)

			if attendee.attendee in found:
				frappe.throw(_("Attendee {0} enterd twice").format(attendee.attendee))
			
			found.append(attendee.attendee)

# mark this function as whitelist
@frappe.whitelist()
def get_full_name(attendee):
	user = frappe.get_doc("User", attendee)
	# concatenates by space if it has value
	return " ".join(filter(None, [user.first_name, user.middle_name, user.last_name]))
