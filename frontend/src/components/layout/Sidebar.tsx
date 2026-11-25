
import {
    Drawer,
    List,
    ListItemButton,
    ListItemIcon,
    ListItemText,
    Toolbar
} from "@mui/material";

import DashboardIcon from "@mui/icons-material/Dashboard";
import RouterIcon from "@mui/icons-material/Router";
import WifiIcon from "@mui/icons-material/Wifi";
import DevicesIcon from "@mui/icons-material/Devices";
import AssessmentIcon from "@mui/icons-material/Assessment";
import SecurityIcon from "@mui/icons-material/Security";
import NotificationsIcon from "@mui/icons-material/Notifications";
import PeopleIcon from "@mui/icons-material/People";
import SettingsIcon from "@mui/icons-material/Settings";

import { Link } from "react-router-dom";
import { useAuth } from "../../contexts/AuthContext";

const drawerWidth = 240;

const menus = [

    { text: "Dashboard", icon: <DashboardIcon />, path: "/dashboard", roles: ["admin", "manager", "technician", "viewer"] },
    { text: "Routers", icon: <RouterIcon />, path: "/routers", roles: ["admin", "manager", "technician", "viewer"] },
    { text: "Networks", icon: <WifiIcon />, path: "/networks", roles: ["admin", "manager"] },
    { text: "Devices", icon: <DevicesIcon />, path: "/devices", roles: ["admin", "manager", "technician"] },
    { text: "Monitoring", icon: <AssessmentIcon />, path: "/monitoring", roles: ["admin", "manager", "technician"] },
    { text: "Reports", icon: <AssessmentIcon />, path: "/reports", roles: ["admin", "manager"] },
    { text: "Security", icon: <SecurityIcon />, path: "/security", roles: ["admin"] },
    { text: "Notifications", icon: <NotificationsIcon />, path: "/notifications", roles: ["admin", "manager", "technician", "viewer"] },
    { text: "Users", icon: <PeopleIcon />, path: "/users", roles: ["admin"] },
    { text: "Settings", icon: <SettingsIcon />, path: "/settings", roles: ["admin"] }

];

export default function Sidebar({ horizontal = false }: { horizontal?: boolean }) {
    const { user } = useAuth();
    const visibleMenus = menus.filter((menu) =>
        user?.role && menu.roles.includes(user.role)
    );

    return (

        <Drawer
            variant="permanent"
            sx={{
                width: horizontal ? "100%" : drawerWidth,
                "& .MuiDrawer-paper": {
                    width: horizontal ? "100%" : drawerWidth,
                    position: horizontal ? "static" : "fixed",
                    boxSizing: "border-box",
                    flexDirection: horizontal ? "row" : "column",
                    alignItems: horizontal ? "center" : "stretch",
                    overflowX: horizontal ? "auto" : "visible"
                }
            }}
        >

            {!horizontal && <Toolbar />}

            <List sx={{
                display: horizontal ? "flex" : "block",
                alignItems: "center",
                py: horizontal ? 0 : undefined
            }}>

                {visibleMenus.map((menu) => (

                    <ListItemButton
                        component={Link}
                        to={menu.path}
                        key={menu.text}
                        sx={{
                            whiteSpace: "nowrap",
                            px: horizontal ? 1.5 : undefined
                        }}
                    >

                        <ListItemIcon>

                            {menu.icon}

                        </ListItemIcon>

                        <ListItemText primary={menu.text} />

                    </ListItemButton>

                ))}

            </List>

        </Drawer>

    );

}