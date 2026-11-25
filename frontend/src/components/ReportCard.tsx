import {

Card,
CardContent,
Typography,
Button,
Stack

} from "@mui/material";

export default function ReportCard({

title,

action

}:any){

return(

<Card>

<CardContent>

<Typography variant="h6">

{title}

</Typography>

<Stack sx={{ mt: 2 }}>

<Button

variant="contained"

onClick={action}

>

Generate

</Button>

</Stack>

</CardContent>

</Card>

);

}