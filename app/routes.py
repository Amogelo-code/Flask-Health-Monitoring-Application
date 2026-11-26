import os

def index(app):
    @app.route('/')
    def home():
        return{ "app name": "Health Monitoring Application",
                "environment": os.getenv("ENVIRONMENT", "dev"),
                "welcome text": "Welcome to Health Monitoring Application",
                }
    @app.route('/health')
    def health():
        return{ "status": "healthy"}, 200
    @app.route('/info')
    def info():
        return{ "app name": "Health Monitoring Application",
                "version": os.getenv("APP_VERSION", "1.0.0"),
                "info": "The first version of the application",
                }
