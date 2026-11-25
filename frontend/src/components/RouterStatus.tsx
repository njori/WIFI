import {

Card,
Typography,
Chip,
Stack

} from "@mui/material";

export default function RouterStatus({routers}:any){

return(

<Card sx={{p:2}}>

<Typography variant="h6">

Router Status

</Typography>

<Stack component="div" spacing={1} sx={{ mt: 2 }}>

{

routers.map((router:any)=>(

<Chip

key={router.id}

label={`${router.name} (${router.ip_address})`}

color={

router.is_online

?

"success"

:

"error"

}

/>

))

}

</Stack>

</Card>

);

}