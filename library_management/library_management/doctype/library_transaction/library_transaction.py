import frappe
from frappe.model.document import Document


class LibraryTransaction(Document):

    def validate(self):
        article = frappe.get_doc(
            "Library Article", self.library_article
        )

        if self.transaction_type == "Issue":
            if article.status == "Issued":
                frappe.throw("This article is already issued.")

        elif self.transaction_type == "Return":
            if article.status != "Issued":
                frappe.throw("This article is not currently issued.")

    def on_submit(self):
        article = frappe.get_doc(
            "Library Article", self.library_article
        )

        if self.transaction_type == "Issue":
            article.status = "Issued"

        elif self.transaction_type == "Return":
            article.status = "Available"

        article.save()