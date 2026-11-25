import {
Dialog,
DialogTitle,
DialogContent,
Stack,
TextField,
Button,
MenuItem
} from "@mui/material";

import {useEffect,useState} from "react";
import AvatarUpload from "../common/AvatarUpload";

const roles = [
    { value: "admin", label: "Admin" },
    { value: "manager", label: "Manager" },
    { value: "technician", label: "Technician" },
    { value: "viewer", label: "Viewer" }
];

export default function UserDialog({

open,
user,
onClose,
onSave

}:any){

const[form,setForm]=useState({

full_name:"",
username:"",
email:"",
phone:"",
role:"viewer"

});

useEffect(()=>{

if(user){

setForm(user);

}else{

setForm({
    full_name:"",
    username:"",
    email:"",
    phone:"",
    role:"viewer"
});

}

},[user]);

function change(e:any){

setForm({

...form,

[e.target.name]:e.target.value

});

}

return(

<Dialog

open={open}

onClose={onClose}

fullWidth

>

<DialogTitle>

User

</DialogTitle>

<DialogContent>

<Stack spacing={2} sx={{ mt: 2 }}>

<TextField

label="Full Name"

name="full_name"

value={form.full_name}

onChange={change}

/>

            <AvatarUpload />
        
<TextField
label="Username"
name="username"
value={form.username}
onChange={change}
/>
<TextField
label="Email"
name="email"
value={form.email}
onChange={change}
/>
<TextField
label="Phone"
name="phone"
value={form.phone}
onChange={change}
/>
<TextField
select
label="Role"
name="role"
value={form.role}
onChange={change}
>
{roles.map((role) => (
<MenuItem key={role.value} value={role.value}>
{role.label}
</MenuItem>
))}

</TextField>

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