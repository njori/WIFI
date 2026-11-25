import {
    Dashboard,
    Router,
    Wifi,
    Devices,
    Monitor,
    Description,
    Notifications,
    Security,
    Settings
} from "@mui/icons-material";

import { NavLink } from "react-router-dom";

const menus = [

    {
        title: "Dashboard",
        icon: <Dashboard />,
        path: "/dashboard"
    },

    {
        title: "Routers",
        icon: <Router />,
        path: "/routers"
    },

    {
        title: "Networks",
        icon: <Wifi />,
        path: "/networks"
    },

    {
        title: "Devices",
        icon: <Devices />,
        path: "/devices"
    },

    {
        title: "Monitoring",
        icon: <Monitor />,
        path: "/monitoring"
    },

    {
        title: "Reports",
        icon: <Description />,
        path: "/reports"
    },

    {
        title: "Notifications",
        icon: <Notifications />,
        path: "/notifications"
    },

    {
        title: "Security",
        icon: <Security />,
        path: "/security"
    },

    {
        title: "Settings",
        icon: <Settings />,
        path: "/settings"
    }

];

export default function Sidebar() {

    return (

        <aside
            style={{
                width: 250,
                background: "#1e293b",
                color: "white",
                padding: 20
            }}
        >

            <h2>WiFi Manager</h2>

            <br />

            {menus.map((menu) => (

                <NavLink
                    key={menu.path}
                    to={menu.path}
                    style={{
                        display: "flex",
                        alignItems: "center",
                        gap: 10,
                        color: "white",
                        padding: 12
                    }}
                >

                    {menu.icon}

                    {menu.title}

                </NavLink>

            ))}

        </aside>

    );

}