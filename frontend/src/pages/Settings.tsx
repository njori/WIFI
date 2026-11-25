import {

Grid,
Button

} from "@mui/material";

import {

useEffect,
useState

} from "react";

import GeneralSettings from "../components/GeneralSettings";
import MailSettings from "../components/MailSettings";
import NotificationSettings from "../components/NotificationSettings";
import ThemeSettings from "../components/ThemeSettings";
import BackupSettings from "../components/BackupSettings";

import {

SettingsService

} from "../services/settingsService";

export default function Settings(){

const[form,setForm]=useState<any>({});

async function load(){

setForm(

await SettingsService.get()

);

}

useEffect(()=>{

load();

},[]);

function change(e:any){

setForm({

...form,

[e.target.name]:e.target.value

});

}

return(

<Grid container spacing={3}>

<Grid size={{ xs:12, md:6 }}>

<GeneralSettings

form={form}

change={change}

/>

</Grid>

<Grid size={{ xs:12, md:6 }}>

<MailSettings

form={form}

change={change}

/>

</Grid>

<Grid size={{ xs:12 }}>

<NotificationSettings

form={form}

change={change}

/>

</Grid>

<Grid size={{ xs:12 }}>

<ThemeSettings

form={form}

change={change}

/>

</Grid>

<Grid size={{ xs:12 }}>

<BackupSettings

backup={()=>SettingsService.backup()}

restore={()=>SettingsService.restore()}

/>

</Grid>

<Grid size={{ xs:12 }}>

<Button

variant="contained"

onClick={()=>SettingsService.save(form)}

>

Save Settings

</Button>

</Grid>

</Grid>

);

}