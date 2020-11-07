# Final Project

Web Programming with Python and JavaScript

For my final project, I created an invoice tracking system with Django and Javascript. The user is first guided to the login page to log in. When logged in, the user is brought to the home page with a list of invoices that have been registered. The invoice table, made with a list view, has columns for the invoice number, purchase order number, customer, and the date that the order was made. Clicking on the invoice number will display the details of the invoice, and there the user can add items to the invoice, edit items or edit the details of the invoice itself. Items or the invoice itself can also be deleted. On this tab, there are two buttons: the "New Invoice" button and the "Search" button. Clicking the new invoice button creates a new invoice. The search button allows the user to search for an invoice by the customer and/or a range of dates, and the datepicker is written in Javascript. The results also have hyperlinks to access the details of he invoices listed. There is also a contract management tab that lists all the contracts made (along with the start and end date) and the invoices associated with the contracts. Like for the invoice table, clicking the invoice number leads to details about the invoice and the items. If a user is logged in and they close the window, they will still be logged in the next time. Clicking the logout button will log out the user and return the user to the login page.

What is in each file:
-erp/views.py: manages the login view and redirects the user to the home page when logged in.
-erp/static/erp/main.css: Styling for the website in general.
-erp/static/erp/(other three files): The javascript and css for making datepickers.
-erp/templates/erp/base.html: The layout for all the html pages in the website (nav bar etc.)
-erp/templates/erp/login.html: The login page.
-erp/templates/erp/logout.html: Contains javascript to make the website sleep for a moment before redirecting the user to the login page.
-invoice/forms.py: Contains the form to make a new invoice and new item.
-invoice/models.py: Contains the models used to store information (Invoice, Order, Customer etc.)
-invoice/views.py: Facilitates the views associated with the invoice tab (new invoice, new item, search etc.)
-invoice/templates/invoice/detail.html: Contains the page for displaying the details of each invoice.
-invoice/templates/invoice/home.html: Contains the page for listing all the invoices.
-invoice/templates/invoice/invoice_confirm_delete.html: Asks the user if they really want to delete an invoice as a safety barrier.
-invoice/templates/invoice/order_confirm_delete.html: Same as above but for orders.
-invoice/templates/invoice/invoice_form.html: Webpage that creates a new invoice.
-invoice/templates/invoice/order_form.html: Webpage that creates a new order.
-invoice/templates/invoice/search.html: Webpage that searches for an invoice by a range of dates and/or by customer.
-cmt/views.py: Redirects the user to the list of contracts.
-cmt/templates/cmt/home.html: Webpage that displays the list of contracts.