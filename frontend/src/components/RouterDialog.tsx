import {

Dialog,

DialogTitle,

DialogContent,

TextField,

Button,

Stack

} from "@mui/material";

import { useState,useEffect } from "react";

export default function RouterDialog({

open,

router,

onClose,

onSave

}:any){

const[form,setForm]=useState({

name:"",

ip_address:"",

username:"",

password:"",

location:""

});

useEffect(()=>{

if(router){

setForm(router);

}

},[router]);

function change(e:any){

setForm({

...form,

[e.target.name]:e.target.value

});

}

return(

<Dialog open={open} onClose={onClose} fullWidth>

<DialogTitle>

Router

</DialogTitle>

<DialogContent>

<Stack component="div" spacing={2} sx={{ mt: 2 }}>

<TextField

label="Name"

name="name"

value={form.name}

onChange={change}

/>

<TextField

label="IP Address"

name="ip_address"

value={form.ip_address}

onChange={change}

/>

<TextField

label="Username"

name="username"

value={form.username}

onChange={change}

/>

<TextField

label="Password"

type="password"

name="password"

value={form.password}

onChange={change}

/>

<TextField

label="Location"

name="location"

value={form.location}

onChange={change}

/>

<Button

variant="contained"

onClick={()=>onSave(form)}

>

Save

</Button>

</Stack>

</DialogContent>

</Dialog>

);

}