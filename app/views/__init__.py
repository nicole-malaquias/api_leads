from flask import Flask

def init_app(app: Flask):
    
    from app.views.route_lead import bp_lead
    app.register_blueprint(bp_lead)

