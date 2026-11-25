import {
    Breadcrumbs,
    Typography
} from "@mui/material";

import NavigateNextIcon from "@mui/icons-material/NavigateNext";

import { Link } from "react-router-dom";

export default function PageBreadcrumbs({

    page

}: any) {

    return (

        <Breadcrumbs
            separator={<NavigateNextIcon fontSize="small" />}
        >

            <Link to="/">

                Dashboard

            </Link>

            <Typography>

                {page}

            </Typography>

        </Breadcrumbs>

    );

}