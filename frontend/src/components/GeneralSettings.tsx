import {
Card,
CardContent,
TextField,
Stack
} from "@mui/material";

export default function GeneralSettings({

form,

change

}:any){

return(

<Card>

<CardContent>

<Stack spacing={2}>

<TextField

label="System Name"

name="system_name"

value={form.system_name}

onChange={change}

/>

<TextField

label="Organization"

name="organization"

value={form.organization}

onChange={change}

/>

<TextField

label="Timezone"

name="timezone"

value={form.timezone}

onChange={change}

/>

<TextField

label="Language"

name="language"

value={form.language}

onChange={change}

/>

</Stack>

</CardContent>

</Card>

);

}