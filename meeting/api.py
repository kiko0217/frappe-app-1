import frappe
from frappe import _
from frappe.utils.data import add_days, nowdate

@frappe.whitelist()
def send_invitation_emails(meeting):
    meeting = frappe.get_doc("Meeting", meeting)
    meeting.check_permission("email")

    if meeting.status == "Planned":
        # frappe.sendmail(
        #     recipients=[d.attendee for d in meeting.attendees],
        #     # sender=frappe.session.user,
        #     subject=meeting.title,
        #     message=meeting.invitation_message,
        #     reference_doctype=meeting.doctype,
        #     reference_name=meeting.name
        # )

        meeting.status = "Invitation Send"
        meeting.save()

        frappe.msgprint(_("Invitation Send"))
    
    else:
        frappe.msgprint(_("Meeting Status must be 'Planned'"))


def make_orientation_meeting(doc, method):
    """Create Orintate"""
    meeting = frappe.get_doc({
        "doctype": "Meeting",
        "title": "Orientation for {0}".format(doc.first_name),
        "date": add_days(nowdate(), 1),
        "from_time": "09:00",
        "to_time": "09:30",
    })
    print("hello")
    print(meeting)