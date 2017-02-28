## ERPNext_plus_Signaturit

An integration of ERPNext and Signaturit

### About

1. config folder contains application configuration info
2. desktop.py is where desktop icons can be added to the Desk
3. hooks.py is where integrations with the environment and other applications is mentioned.
4. library_management (inner) is a module that is bootstrapped. In Frappe, a module is where model and controller files reside.
5. modules.txt contains list of modules in the app. When you create a new module, it is required that you update it in this file.
6. patches.txt is where migration patches are written. They are python module references using the dot notation.
7. templates is the folder where web view templates are maintained. Templates for Login and other standard pages are bootstrapped in frappe.
8. generators are where templates for models are maintained, where each model instance has a separte web route, for example a Blog Post where each post has its unique web url. In Frappe, the templating engine used is Jinja2
9. pages is where single route templates are maintained. For example for a "/blog" type of page.


#### License

MIT