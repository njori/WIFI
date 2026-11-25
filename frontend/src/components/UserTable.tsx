import {

Button,
Chip

} from "@mui/material";

import {

DataGrid,

} from "@mui/x-data-grid";
import type {
    GridColDef
} from "@mui/x-data-grid";

export default function UserTable({

rows,
onEdit,
onDelete,
onStatus,
onHistory

}:any){

const columns:GridColDef[]=[

{field:"full_name",headerName:"Name",flex:1},

{field:"username",headerName:"Username",flex:1},

{field:"email",headerName:"Email",flex:1},

{
field:"role",
headerName:"Role",
flex:1,
valueFormatter:(value:string) =>
    value.charAt(0).toUpperCase() + value.slice(1)
},

{

field:"status",

headerName:"Status",

flex:1,

renderCell:(params)=>(

<Chip

label={params.value}

color={

params.value==="Active"

?

"success"

:

"error"

}

/>

)

},

{field:"last_login",headerName:"Last Login",flex:1},

{

field:"actions",

headerName:"Actions",

flex:2,

renderCell:(params)=>(

<>

<Button onClick={()=>onEdit(params.row)}>

Edit

</Button>

<Button onClick={()=>onHistory(params.row)}>

History

</Button>

<Button onClick={()=>onStatus(params.row.id)}>

Status

</Button>

<Button

color="error"

onClick={()=>onDelete(params.row.id)}

>

Delete

</Button>

</>

)

}

];

return(

<div style={{height:650}}>

<DataGrid

rows={rows}

columns={columns}

pageSizeOptions={[10,25,50]}

/>

</div>

);

}