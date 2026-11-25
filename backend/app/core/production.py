import logging
from flask import jsonify, request

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# -----------------------------
# Success Response
# -----------------------------
def success(message="", data=None):

    return jsonify({
        "success": True,
        "message": message,
        "data": data
    })


# -----------------------------
# Error Response
# -----------------------------
def error(message="", status=400):

    return jsonify({
        "success": False,
        "message": message
    }), status


# -----------------------------
# Pagination
# -----------------------------
def paginate(query, page, per_page):

    result = query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )

    return {
        "items": [item.to_dict() for item in result.items],
        "page": result.page,
        "pages": result.pages,
        "total": result.total
    }


# -----------------------------
# Validate Required Fields
# -----------------------------
def validate(data, fields):

    for field in fields:

        if field not in data or data[field] == "":
            raise Exception(f"{field} is required.")


# -----------------------------
# Global Error Handler
# -----------------------------
def register_error_handler(app):

    @app.errorhandler(Exception)
    def handle_exception(e):

        logger.error(str(e))

        return jsonify({
            "success": False,
            "message": str(e)
        }), 400


# -----------------------------
# Log Request
# -----------------------------
def log_request():

    logger.info(
        f"{request.method} {request.path}"
    )


# -----------------------------
# Health Check
# -----------------------------
def health():

    return {
        "status": "OK",
        "service": "WiFi Management Backend"
    }