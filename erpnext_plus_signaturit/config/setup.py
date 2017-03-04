from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Settings"),
            "icon": "octicon octicon-cloud-upload",
            "items": [
                {
                    "type": "doctype",
                    "name": "Settings",
                    "label": _("ERPNext plus Signaturit"),
                    "description": _("Integration of ERPNext and Signaturit"),
                    "hide_count": True
                }
            ]
        }
    ]
