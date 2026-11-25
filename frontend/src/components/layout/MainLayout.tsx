import {
    Box,
    Toolbar
} from "@mui/material";

import Sidebar from "./Sidebar";
import Navbar from "./Navbar";
import Footer from "./Footer";

export default function MainLayout({

    children

}: any) {

    return (

        <Box
            sx={{
                display: "flex"
            }}
        >

            <Navbar />

            <Sidebar />

            <Box
                component="main"
                sx={{
                    flexGrow: 1,
                    p: 3
                }}
            >

                <Toolbar />

                {children}

                <Footer />

            </Box>

        </Box>

    );

}