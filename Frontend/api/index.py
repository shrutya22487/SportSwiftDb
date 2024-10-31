from backend.app import app as application

def handler(event, context):
    # Pass request to Flask app
    return application(event, context)
