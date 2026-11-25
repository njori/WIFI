import {

Card,
CardContent,
Typography

} from "@mui/material";

export default function SecurityCard({

title,

value

}:any){

return(

<Card>

<CardContent>

<Typography variant="h6">

{title}

</Typography>

<Typography variant="h3">

{value}

</Typography>

</CardContent>

</Card>

);

}