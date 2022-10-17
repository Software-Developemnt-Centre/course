```python
# Copyright (c) 2022, SDC and contributors
# For license information, please see license.txt

# import frappe
#from frappe.model.document import Document

#class LibraryTransaction(Document):
#	pass

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
    def before_submit(self):
        if self.type == "Issue":
            self.validate_issue()
            # set the item status to be Issued
            item = frappe.get_doc("Item", self.item)
            item.status = "Issued"
            item.save()

        elif self.type == "Return":
            self.validate_return()
            # set the item status to be Available
            item = frappe.get_doc("Item", self.item)
            item.status = "Available"
            item.save()

    def validate_issue(self):
        self.validate_membership()
        item = frappe.get_doc("Item", self.item)
        # item cannot be issued if it is already issued
        if item.status == "Issued":
            frappe.throw("Item is already issued by another member")

    def validate_return(self):
        item = frappe.get_doc("Item", self.item)
        # item cannot be returned if it is not issued first
        if item.status == "Available":
            frappe.throw("Item cannot be returned without being issued first")

    def validate_membership(self):
        # check if a valid membership exist for this library member
        valid_membership = frappe.db.exists(
            "Library Membership",
            {
                "library_member": self.library_member,
                "docstatus": DocStatus.submitted(),
                "from_date": ("<", self.date),
                "to_date": (">", self.date),
            },
        )
        if not valid_membership:
            frappe.throw("The member does not have a valid membership")
            
            
    def validate_maximum_limit(self):
        max_articles = frappe.db.get_single_value("Library Settings", "max_articles")
        count = frappe.db.count(
            "Library Transaction",
            {"library_member": self.library_member, "type": "Issue", "docstatus": DocStatus.submitted()},
        )
        if count >= max_articles:
            frappe.throw("Maximum limit reached for issuing articles")
```
SDC 
