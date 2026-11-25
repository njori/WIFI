import {

DataGrid,

} from "@mui/x-data-grid";
import type {
    GridColDef
} from "@mui/x-data-grid";

export default function AuditTable({

rows

}:any){

const columns:GridColDef[]=[

{field:"username",headerName:"User",flex:1},

{field:"action",headerName:"Action",flex:2},

{field:"ip_address",headerName:"IP Address",flex:1},

{field:"created_at",headerName:"Time",flex:2}

];

return(

<div style={{height:400}}>

<DataGrid

rows={rows}

columns={columns}

/>

</div>

);

}