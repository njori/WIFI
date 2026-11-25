import {
    AppBar,
    Toolbar,
    Typography,
    Box,
    IconButton
} from "@mui/material";

import MenuIcon from "@mui/icons-material/Menu";
import NotificationsIcon from "@mui/icons-material/Notifications";
import AccountCircleIcon from "@mui/icons-material/AccountCircle";

import ThemeToggle from "../common/ThemeToggle";

export default function Navbar() {

    return (

        <AppBar position="fixed">

            <Toolbar>

                <IconButton color="inherit">

                    <MenuIcon />

                </IconButton>

                <Typography
                    variant="h6"
                    sx={{ flexGrow: 1 }}
                >

                    WiFi Management System

                </Typography>

                <ThemeToggle />

                <Box>

                    <IconButton color="inherit">

                        <NotificationsIcon />

                    </IconButton>

                    <IconButton color="inherit">

                        <AccountCircleIcon />

                    </IconButton>

                </Box>

            </Toolbar>

        </AppBar>

    );

}