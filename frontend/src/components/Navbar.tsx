import { Avatar, Button } from "@mui/material";

import { useAuth } from "../contexts/AuthContext";
import NotificationBadge from "./NotificationBadge";
import { useNavigate } from "react-router-dom";

export default function Navbar() {

    const { user, logout } = useAuth();
    const navigate = useNavigate();

    return (

        <header
            style={{
                background: "white",
                padding: 20,
                display: "flex",
                justifyContent: "space-between",
                alignItems: "center",
                borderBottom: "1px solid #ddd"
            }}
        >

            <h2>Enterprise WiFi Management</h2>

            <div
                style={{
                    display: "flex",
                    alignItems: "center",
                    gap: 15
                }}
            >

                <span>

                    <strong>{user?.username}</strong>
                    <br />
                    <small>
                        {user?.role
                            ? user.role.charAt(0).toUpperCase() + user.role.slice(1)
                            : ""}
                    </small>

                </span>

                <Avatar>

                    {user?.username?.charAt(0)}
                    
                </Avatar>
                <NotificationBadge count={5}/>

                <Button
                    variant="outlined"
                    size="small"
                    onClick={() => {
                        logout();
                        navigate("/login", { replace: true });
                    }}
                >
                    Logout
                </Button>

            </div>

        </header>

    );

}