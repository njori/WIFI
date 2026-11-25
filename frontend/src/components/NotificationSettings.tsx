import {

Card,
CardContent,
FormControlLabel,
Switch

} from "@mui/material";

export default function NotificationSettings({

form,

change

}:any){

return(

<Card>

<CardContent>

<FormControlLabel

control={

<Switch

checked={form.email_notifications}

onChange={(e)=>change({

target:{

name:"email_notifications",

value:e.target.checked

}

})}

/>

}

label="Enable Email Notifications"

/>

</CardContent>

</Card>

);

}