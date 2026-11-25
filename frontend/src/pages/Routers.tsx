import { useEffect,useState } from "react";

import {

Button,

Chip,

Paper

} from "@mui/material";

import {
DataGrid,
} from "@mui/x-data-grid";
import type {
GridColDef
} from "@mui/x-data-grid";

import RouterDialog from "../components/RouterDialog";

import { RouterService } from "../services/routerService";
import { useAuth } from "../contexts/AuthContext";

export default function Routers(){
const { user } = useAuth();

const[data,setData]=useState([]);

const[open,setOpen]=useState(false);

const[selected,setSelected]=useState<any>(null);

async function load(){

const routers=await RouterService.getAll();

setData(user?.role === "technician"
  ? routers.filter((router:any) => !router.is_online || router.needs_maintenance)
  : routers);

}

useEffect(()=>{

load();

},[]);

const columns:GridColDef[]=[

{

field:"name",

headerName:"Router",

flex:1

},

{

field:"ip_address",

headerName:"IP",

flex:1

},

{

field:"manufacturer",

headerName:"Manufacturer",

flex:1

},

{

field:"cpu_usage",

headerName:"CPU",

flex:1

},

{

field:"memory_usage",

headerName:"Memory",

flex:1

},

{

field:"is_online",

headerName:"Status",

flex:1,

renderCell:(params)=>(

<Chip

label={

params.value

?

"Online"

:

"Offline"

}

color={

params.value

?

"success"

:

"error"

}

/>

)

},

{

field:"actions",

headerName:"Actions",

flex:1,

renderCell:(params)=>(
<>
{user?.role !== "viewer" && <Button
onClick={()=>{

setSelected(params.row);

setOpen(true);

}}

>

Edit

</Button>}
 
</>
)

}

];

return(

<Paper sx={{height:700,p:2}}>

{user?.role !== "viewer" && <Button

variant="contained"

onClick={()=>{

setSelected(null);

setOpen(true);

}}

>

Add Router

</Button>}

<DataGrid

rows={data}

columns={columns}

pageSizeOptions={[10]}

/>

<RouterDialog

open={open}

router={selected}

onClose={()=>setOpen(false)}

onSave={async(form:any)=>{

if(selected){

await RouterService.update(

selected.id,

form

);

}else{

await RouterService.create(

form

);

}

setOpen(false);

load();

}}

/>

</Paper>

);

}