# Copyright (c) 2025, Frappe Technologies and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator


class Article(WebsiteGenerator):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		article_name: DF.Data
		author: DF.Data | None
		description: DF.TextEditor | None
		image: DF.AttachImage | None
		isbn: DF.Data | None
		publisher: DF.Data | None
		status: DF.Literal["Issued", "Available"]
	# end: auto-generated types
	pass
