import { useEffect, useState } from "react";

import {

Grid,

Paper,

Typography

} from "@mui/material";

import CpuChart from "../components/CpuChart";
import MemoryChart from "../components/MemoryChart";
import TrafficChart from "../components/TrafficChart";
import RouterStatus from "../components/RouterStatus";

import socket from "../services/socket";
import { MonitoringService } from "../services/monitoringService";

export default function Monitoring(){

const[data,setData]=useState<any>(null);

async function load(){

const res=await MonitoringService.getOverview();

setData(res);

}

useEffect(()=>{

load();

socket.on(

"monitoring",

(payload)=>{

setData(payload);

}

);

return()=>{

socket.off("monitoring");

};

},[]);

if(!data){

return<h2>Loading...</h2>;

}

return(

<Grid container spacing={3}>

<Grid size={{ xs:12, md:6 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

CPU Usage

</Typography>

<CpuChart data={data.cpu_history}/>

</Paper>

</Grid>

<Grid size={{ xs:12, md:6 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

Memory Usage

</Typography>

<MemoryChart data={data.memory_history}/>

</Paper>

</Grid>

<Grid size={{ xs:12 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

Network Traffic

</Typography>

<TrafficChart data={data.traffic_history}/>

</Paper>

</Grid>

<Grid size={{ xs:12 }}>

<RouterStatus routers={data.routers}/>

</Grid>

</Grid>

);

}