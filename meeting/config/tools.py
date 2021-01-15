from __future__ import unicode_literals
from frappe import _


def get_data():
	return [
		# Administration
		{
			"module_name": "Desk",
			"category": "Administration",
			"label": _("Meeting"),
			"color": "#FFF5A7",
			"reverse": 1,
			"icon": "octicon octicon-calendar",
			"type": "module",
			"description": "Todos, notes, calendar and newsletter."
		},
    ]