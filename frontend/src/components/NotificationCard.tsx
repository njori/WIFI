import {

Card,

CardContent,

Typography,

Chip,

Stack,

Button

} from "@mui/material";

export default function NotificationCard({

notification,

onRead,

onDelete

}:any){

return(

<Card sx={{mb:2}}>

<CardContent>

<Stack

direction="row"

sx={{ justifyContent: "space-between" }}

>

<div>

<Typography variant="h6">

{notification.title}

</Typography>

<Typography>

{notification.message}

</Typography>

<Typography

variant="caption"

>

{notification.created_at}

</Typography>

</div>

<Chip

label={notification.level}

color={

notification.level==="error"

?

"error"

:

notification.level==="warning"

?

"warning"

:

notification.level==="success"

?

"success"

:

"info"

}

/>

</Stack>

<Stack

direction="row"

spacing={2}

sx={{ mt: 2 }}

>

<Button

variant="contained"

onClick={()=>onRead(notification.id)}

>

Mark Read

</Button>

<Button

color="error"

onClick={()=>onDelete(notification.id)}

>

Delete

</Button>

</Stack>

</CardContent>

</Card>

);

}