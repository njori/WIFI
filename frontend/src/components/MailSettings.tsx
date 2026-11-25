import {

Card,
CardContent,
Stack,
TextField

} from "@mui/material";

export default function MailSettings({

form,

change

}:any){

return(

<Card>

<CardContent>

<Stack spacing={2}>

<TextField

label="SMTP Server"

name="smtp_server"

value={form.smtp_server}

onChange={change}

/>

<TextField

label="SMTP Port"

name="smtp_port"

value={form.smtp_port}

onChange={change}

/>

<TextField

label="SMTP Username"

name="smtp_username"

value={form.smtp_username}

onChange={change}

/>

<TextField

label="SMTP Password"

type="password"

name="smtp_password"

value={form.smtp_password}

onChange={change}

/>

</Stack>

</CardContent>

</Card>

);

}