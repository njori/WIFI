from flask import jsonify

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


##############################################################
# RATE LIMITER
##############################################################

limiter = Limiter(

    key_func=get_remote_address,

    default_limits=[

        "1000/day",

        "500/hour"

    ],

    storage_uri="memory://"

)


##############################################################
# COMMON LIMITS
##############################################################

LOGIN_LIMIT = "5/minute"

REGISTER_LIMIT = "3/minute"

PASSWORD_RESET_LIMIT = "3/hour"

SCAN_LIMIT = "2/minute"

DISCOVERY_LIMIT = "2/minute"

MONITOR_LIMIT = "10/minute"

CREATE_LIMIT = "30/minute"

UPDATE_LIMIT = "60/minute"

DELETE_LIMIT = "20/minute"

REPORT_LIMIT = "10/hour"

EXPORT_LIMIT = "20/hour"

UPLOAD_LIMIT = "5/hour"

DOWNLOAD_LIMIT = "50/hour"

API_KEY_LIMIT = "30/hour"

ADMIN_LIMIT = "100/hour"

SECURITY_LIMIT = "20/minute"


##############################################################
# CUSTOM ERROR
##############################################################

def register_rate_limit_handler(app):

    @app.errorhandler(429)

    def ratelimit_handler(error):

        return jsonify({

            "success": False,

            "message": "Too many requests.",

            "error": "RATE_LIMIT_EXCEEDED"

        }),429