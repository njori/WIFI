import {
    Box,
    Typography
} from "@mui/material";

export default function Footer() {

    return (

        <Box
            sx={{
                mt: 5,
                py: 2,
                textAlign: "center"
            }}
        >

            <Typography variant="body2">

                © 2026 WiFi Management System

            </Typography>

        </Box>

    );

}