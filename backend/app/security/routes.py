from flask import Blueprint, request, jsonify

from flask_jwt_extended import (
    jwt_required,
    get_jwt_identity
)

from app.security.services import SecurityService
from app.security.decorators import (
    admin_required,
    permission_required
)

security_bp = Blueprint(
    "security",
    __name__,
    url_prefix="/api/security"
)


@security_bp.get("/settings")
def settings():
    return jsonify({
        "status": "healthy",
        "module": "Enterprise Security",
        "version": "1.0",
        "settings": {
            "alerts_enabled": True,
            "threat_detection": True,
            "auto_block": True,
        },
    })

##############################################################
# GET ALL ROLES
##############################################################

@security_bp.get("/roles")
@jwt_required()
@permission_required("view_roles")
def get_roles():

    return jsonify(

        SecurityService.get_roles()

    )


##############################################################
# CREATE ROLE
##############################################################

@security_bp.post("/roles")
@jwt_required()
@admin_required
def create_role():

    data = request.json

    return jsonify(

        SecurityService.create_role(data)

    ),201


##############################################################
# UPDATE ROLE
##############################################################

@security_bp.put("/roles/<int:role_id>")
@jwt_required()
@admin_required
def update_role(role_id):

    return jsonify(

        SecurityService.update_role(

            role_id,

            request.json

        )

    )


##############################################################
# DELETE ROLE
##############################################################

@security_bp.delete("/roles/<int:role_id>")
@jwt_required()
@admin_required
def delete_role(role_id):

    return jsonify(

        SecurityService.delete_role(

            role_id

        )

    )

##############################################################
# GET PERMISSIONS
##############################################################

@security_bp.get("/permissions")
@jwt_required()
def permissions():

    return jsonify(

        SecurityService.get_permissions()

    )


##############################################################
# CREATE PERMISSION
##############################################################

@security_bp.post("/permissions")
@jwt_required()
@admin_required
def create_permission():

    return jsonify(

        SecurityService.create_permission(

            request.json

        )

    )


##############################################################
# ASSIGN PERMISSION
##############################################################

@security_bp.post("/roles/<int:role_id>/permissions/<int:permission_id>")
@jwt_required()
@admin_required
def assign_permission(

    role_id,

    permission_id

):

    return jsonify(

        SecurityService.assign_permission(

            role_id,

            permission_id

        )

    )


##############################################################
# REVOKE PERMISSION
##############################################################

@security_bp.delete("/roles/<int:role_id>/permissions/<int:permission_id>")
@jwt_required()
@admin_required
def revoke_permission(

    role_id,

    permission_id

):

    return jsonify(

        SecurityService.revoke_permission(

            role_id,

            permission_id

        )

    )
##############################################################
# ALL AUDITS
##############################################################

@security_bp.get("/audit")
@jwt_required()
@permission_required("view_audit")
def audits():

    return jsonify(

        SecurityService.get_audits()

    )


##############################################################
# USER AUDITS
##############################################################

@security_bp.get("/audit/user/<int:user_id>")
@jwt_required()
def user_audits(user_id):

    return jsonify(

        SecurityService.get_user_audits(

            user_id

        )

    )
##############################################################
# MY SESSIONS
##############################################################

@security_bp.get("/sessions")
@jwt_required()
def sessions():

    user = get_jwt_identity()

    return jsonify(

        SecurityService.get_sessions(

            user

        )

    )


##############################################################
# REVOKE SESSION
##############################################################

@security_bp.delete("/sessions/<token>")
@jwt_required()
def revoke_session(token):

    SecurityService.revoke_session(

        token

    )

    return jsonify({

        "message":"Session revoked."

    })


##############################################################
# REVOKE ALL
##############################################################

@security_bp.delete("/sessions")
@jwt_required()
def revoke_all():

    SecurityService.revoke_all_sessions(

        get_jwt_identity()

    )

    return jsonify({

        "message":"All sessions revoked."

    })

##############################################################
# CREATE API KEY
##############################################################

@security_bp.post("/api-keys")
@jwt_required()
def api_key():

    user = get_jwt_identity()

    return jsonify(

        SecurityService.create_api_key(

            user,

            request.json["name"]

        )

    )


##############################################################
# REVOKE API KEY
##############################################################

@security_bp.delete("/api-keys/<key>")
@jwt_required()
def revoke_api_key(key):

    SecurityService.revoke_api_key(

        key

    )

    return jsonify({

        "message":"API Key revoked."

    })

##############################################################
# REQUEST RESET
##############################################################

@security_bp.post("/forgot-password")
def forgot():

    token = SecurityService.request_password_reset(

        request.json["email"]

    )

    return jsonify({

        "token":token

    })


##############################################################
# RESET PASSWORD
##############################################################

@security_bp.post("/reset-password")
def reset():

    SecurityService.reset_password(

        request.json

    )

    return jsonify({

        "message":"Password updated."

    })
##############################################################
# ENABLE 2FA
##############################################################

@security_bp.post("/2fa")
@jwt_required()
def enable_2fa():

    user = get_jwt_identity()

    secret = SecurityService.enable_2fa(

        user

    )

    return jsonify({

        "secret":secret

    })


##############################################################
# VERIFY OTP
##############################################################

@security_bp.post("/2fa/verify")
@jwt_required()
def verify_2fa():

    user = get_jwt_identity()

    valid = SecurityService.verify_2fa(

        user,

        request.json["code"]

    )

    return jsonify({

        "valid":valid

    })
    ##############################################################
# WHITELIST
##############################################################

@security_bp.post("/whitelist")
@jwt_required()
@admin_required
def whitelist():

    return jsonify(

        SecurityService.add_whitelist(

            request.json

        )

    )


##############################################################
# BLACKLIST
##############################################################

@security_bp.post("/blacklist")
@jwt_required()
@admin_required
def blacklist():

    return jsonify(

        SecurityService.add_blacklist(

            request.json

        )

    )
##############################################################
# PASSWORD CHECK
##############################################################

@security_bp.post("/validate-password")
def validate_password():

    SecurityService.validate_password(

        request.json["password"]

    )

    return jsonify({

        "valid":True

    })
##############################################################
# SECURITY STATUS
##############################################################

@security_bp.get("/status")
@jwt_required()
def status():

    return jsonify({

        "status":"healthy",

        "module":"Enterprise Security",

        "version":"1.0"

    })
