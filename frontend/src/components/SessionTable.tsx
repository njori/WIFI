import {

Button

} from "@mui/material";

import {

DataGrid,

} from "@mui/x-data-grid";
import type {
    GridColDef
} from "@mui/x-data-grid";

export default function SessionTable({

rows,

onTerminate

}:any){

const columns:GridColDef[]=[

{field:"username",headerName:"User",flex:1},

{field:"ip_address",headerName:"IP",flex:1},

{field:"login_time",headerName:"Login Time",flex:2},

{

field:"action",

headerName:"Action",

flex:1,

renderCell:(params)=>(

<Button

color="error"

onClick={()=>onTerminate(params.row.id)}

>

Terminate

</Button>

)

}

];

return(

<div style={{height:350}}>

<DataGrid

rows={rows}

columns={columns}

/>

</div>

);

}