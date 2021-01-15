// Copyright (c) 2021, Fusi and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Meeting', {
// 	refresh: () => {
// 		console.log('hello ini Meeting')
// 	}
// 	// refresh: function(frm) {

// 	// }
// });


frappe.ui.form.on('Meeting', {
	send_emails: (frm) => {
		console.log("test")
		if (frm.doc.status == "Planned") {
			frappe.call({
				method: "meeting.api.send_invitation_emails",
				args: {
					meeting: frm.doc.name
				},
				// callback: (r) => {

				// }
			})
		}
	},
})

frappe.ui.form.on('Meeting Attendee', {
	attendee: (frm, cdt, cdn) => {
		// console.log(frm)
		var attendee = frappe.model.get_doc(cdt, cdn)
		if (attendee.attendee) {
			// if attendee , get full name
			frappe.call({
				method: "meeting.meeting.doctype.meeting.meeting.get_full_name",
				args: {
					attendee: attendee.attendee
				},
				callback: (r) => {
					frappe.model.set_value(cdt, cdn, "full_name", r.message)
				}
			})
		} else {
			// if no attendee, clear full name
			frappe.model.set_value(cdt, cdn, "full_name", null)
		}
	},
	// refresh: function(frm) {

	// }
});

