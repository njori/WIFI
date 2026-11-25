import {
    Box
} from "@mui/material";

export default function PageContainer({

    children

}: any) {

    return (

        <Box
            sx={{
                p: 3
            }}
        >

            {children}

        </Box>

    );

}