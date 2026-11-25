import {

Paper,

Button

} from "@mui/material";

import {

DataGrid,

} from "@mui/x-data-grid";
import type {
    GridColDef
} from "@mui/x-data-grid";

export default function ReportHistory({

rows

}:any){

const columns:GridColDef[]=[

{

field:"title",

headerName:"Report",

flex:1

},

{

field:"report_type",

headerName:"Type",

flex:1

},

{

field:"created_at",

headerName:"Created",

flex:1

},

{

field:"file_name",

headerName:"File",

flex:1

},

{

field:"download",

headerName:"Download",

flex:1,

renderCell:(params)=>(

<Button

href={`http://127.0.0.1:5000/reports/${params.row.file_name}`}

>

Download

</Button>

)

}

];

return(

<Paper sx={{height:500}}>

<DataGrid

rows={rows}

columns={columns}

/>

</Paper>

);

}