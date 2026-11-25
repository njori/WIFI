import { useEffect,useState } from "react";
import { Button, Paper } from "@mui/material";

import UserDialog from "../components/UserDialog";
import UserTable from "../components/UserTable";
import LoginHistoryDialog from "../components/LoginHistoryDialog";
import { UserService } from "../services/userService";
import PageAnimation from "../components/common/PageAnimation";
import { Navigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";


export default function Users(){
const { user } = useAuth();

if (user?.role !== "admin") {
    return <Navigate to="/dashboard" replace />;
}

const[users,setUsers]=useState([]);
const[open,setOpen]=useState(false);
const[selected,setSelected]=useState<any>(null);

const[history,setHistory]=useState([]);
const[historyOpen,setHistoryOpen]=useState(false);

async function load(){

setUsers(

await UserService.getAll()

);

}

useEffect(()=>{

load();

},[]);

return(
<PageAnimation>
<Paper sx={{p:2}}>

<Button

variant="contained"

onClick={()=>{

setSelected(null);

setOpen(true);

}}

>

Add User

</Button>

<UserTable

rows={users}

onEdit={(user:any)=>{

setSelected(user);

setOpen(true);

}}

onDelete={async(id:number)=>{

await UserService.remove(id);

load();

}}

onStatus={async(id:number)=>{

await UserService.toggleStatus(id);

load();

}}

onHistory={async(user:any)=>{

setHistory(

await UserService.history(user.id)

);

setHistoryOpen(true);

}}

/>

<UserDialog

open={open}

user={selected}

onClose={()=>setOpen(false)}

onSave={async(form:any)=>{

if(selected){

await UserService.update(selected.id,form);

}else{

await UserService.create(form);

}

setOpen(false);

load();

}}

/>

<LoginHistoryDialog

open={historyOpen}

history={history}

onClose={()=>setHistoryOpen(false)}

/>

</Paper>
</PageAnimation>
);

}