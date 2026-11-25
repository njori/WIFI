from app.routes.health import health_bp
from app.routes.auth import auth_bp
from app.routes.dashboard import dashboard_bp
from app.routes.router import router_bp
from app.routes.network import network_bp
from app.routes.device import device_bp
from app.routes.log import log_bp
from app.routes.notification import notification_bp
from app.routes.discovery import discovery_bp
from app.routes.monitor import monitor_bp
from app.routes.topology import topology_bp
from app.routes.report import report_bp
from app.routes.security import security_bp
from app.routes.analytics import analytics_bp
from app.routes.traffic import traffic_bp
from app.routes.intrusion import intrusion_bp
from app.routes.automation import automation_bp
from app.routes.settings import settings_bp
from app.routes.user import user_bp


def register_routes(app):
    app.register_blueprint(health_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(router_bp)
    app.register_blueprint(network_bp)
    app.register_blueprint(device_bp)
    app.register_blueprint(log_bp)
    app.register_blueprint(notification_bp)
    app.register_blueprint(discovery_bp)
    app.register_blueprint(monitor_bp)
    app.register_blueprint(topology_bp)
    app.register_blueprint(report_bp)
    app.register_blueprint(security_bp)
    app.register_blueprint(analytics_bp)
    app.register_blueprint(traffic_bp)
    app.register_blueprint(intrusion_bp)
    app.register_blueprint(automation_bp)
    app.register_blueprint(settings_bp)
    app.register_blueprint(user_bp)