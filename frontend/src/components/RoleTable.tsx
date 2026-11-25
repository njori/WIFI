import { DataGrid } from "@mui/x-data-grid";
import type { GridColDef } from "@mui/x-data-grid";
import { Chip, Stack } from "@mui/material";

export default function RoleTable({

rows

}:any){

const columns:GridColDef[]=[

{
field:"name",
headerName:"Role",
flex:1,
valueFormatter:(value:string) =>
    value.charAt(0).toUpperCase() + value.slice(1)
},

{field:"description",headerName:"Description",flex:2},

{
field:"permissions",
headerName:"Permissions",
flex:3,
renderCell:(params)=>(
    <Stack direction="row" spacing={0.5} sx={{ flexWrap:"wrap", py:0.5 }}>
        {(params.value || []).map((permission:string) => (
            <Chip key={permission} label={permission} size="small" />
        ))}
    </Stack>
)
}

];

return(

<div style={{height:300}}>

<DataGrid

rows={rows}

columns={columns}

/>

</div>

);

}