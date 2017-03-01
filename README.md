## ERPNext_plus_Signaturit

An integration of ERPNext and Signaturit

### Files in the app

# hooks.py

The hooks.py file defines the metadata of your app and integration points with other parts of Frappe or Frappe apps. Examples of such parts include task scheduling or listening to updates to different documents in the system. For now, it just contains the details you entered during app creation.

```
app_name = "sample-app"
app_title = "Sample App"
app_publisher = "Acme Inc."
app_description = "This is a sample app."
app_icon = "fa-linux"
app_color = "black"
app_email = "info@example.com"
app_url = "http://example.com"
app_version = 0.0.1
modules.txt
```

# modules.txt

Modules in Frappe help you organize Documents in Frappe and they are defined in the modules.txt file in your app. It is necessary for every [DocType] to be attached to a module. By default a module by the name of your app is added. Also, each module gets an icon on the [Desk]. For example, the [ERPNext] app is organized in the following modules.

```
accounts
buying
home
hr
manufacturing
projects
selling
setup
stock
support
utilities
contacts
```

# Others
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