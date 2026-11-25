import {

Card,
CardContent,
Button,
Stack

} from "@mui/material";

export default function BackupSettings({

backup,

restore

}:any){

return(

<Card>

<CardContent>

<Stack

direction="row"

spacing={2}

>

<Button

variant="contained"

onClick={backup}

>

Create Backup

</Button>

<Button

color="warning"

variant="contained"

onClick={restore}

>

Restore Backup

</Button>

</Stack>

</CardContent>

</Card>

);

}