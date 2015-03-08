# myproject/app.py
from oscar.app import Shop
from oscar.core.application import Application

class MyShop(Shop):

    # Override the core dashboard_app instance to use a blank application
    # instance.  This means no dashboard URLs are included.
    dashboard_app = Application()