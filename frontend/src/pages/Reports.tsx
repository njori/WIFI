import {

Grid,

Snackbar

} from "@mui/material";

import {

useEffect,

useState

} from "react";

import ReportCard from "../components/ReportCard";
import ReportHistory from "../components/ReportHistory";

import {

ReportService

} from "../services/reportService";

export default function Reports(){

const[history,setHistory]=useState([]);

const[msg,setMsg]=useState("");

async function load(){

const data=await ReportService.history();

setHistory(data);

}

useEffect(()=>{

load();

},[]);

async function generate(

type:string

){

switch(type){

case"pdf":

await ReportService.generatePDF();

break;

case"excel":

await ReportService.generateExcel();

break;

case"csv":

await ReportService.generateCSV();

break;

case"json":

await ReportService.generateJSON();

break;

}

setMsg("Report generated");

load();

}

return(

<>

<Grid container spacing={3}>

<Grid size={{ xs:12, md:3 }}>

<ReportCard

title="PDF Report"

action={()=>generate("pdf")}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<ReportCard

title="Excel Report"

action={()=>generate("excel")}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<ReportCard

title="CSV Report"

action={()=>generate("csv")}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<ReportCard

title="JSON Report"

action={()=>generate("json")}

/>

</Grid>

<Grid size={{ xs:12 }}>

<ReportHistory

rows={history}

reload={load}

/>

</Grid>

</Grid>

<Snackbar

open={msg!==""}

message={msg}

autoHideDuration={3000}

onClose={()=>setMsg("")}

/>

</>

);

}