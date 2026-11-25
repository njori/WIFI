import {

Grid,

Paper,

Typography

} from "@mui/material";

import {

useEffect,

useState

} from "react";

import SecurityCard from "../components/SecurityCard";
import AuditTable from "../components/AuditTable";
import RoleTable from "../components/RoleTable";
import SessionTable from "../components/SessionTable";

import {

SecurityService

} from "../services/securityService";

export default function Security(){

const[dashboard,setDashboard]=useState<any>({});

const[audit,setAudit]=useState([]);

const[roles,setRoles]=useState([]);

const[sessions,setSessions]=useState([]);

async function load(){

setDashboard(

await SecurityService.dashboard()

);

setAudit(

await SecurityService.auditLogs()

);

setRoles(

await SecurityService.roles()

);

setSessions(

await SecurityService.sessions()

);

}

useEffect(()=>{

load();

},[]);

return(

<Grid container spacing={3}>

<Grid size={{ xs:12, md:3 }}>

<SecurityCard

title="Failed Logins"

value={dashboard.failed_logins||0}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<SecurityCard

title="Locked Accounts"

value={dashboard.locked_accounts||0}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<SecurityCard

title="2FA Enabled"

value={dashboard.two_factor||0}

/>

</Grid>

<Grid size={{ xs:12, md:3 }}>

<SecurityCard

title="Active Sessions"

value={dashboard.active_sessions||0}

/>

</Grid>

<Grid size={{ xs:12 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

Audit Logs

</Typography>

<AuditTable rows={audit}/>

</Paper>

</Grid>

<Grid size={{ xs:12, md:6 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

Roles

</Typography>

<RoleTable rows={roles}/>

</Paper>

</Grid>

<Grid size={{ xs:12, md:6 }}>

<Paper sx={{p:2}}>

<Typography variant="h6">

Active Sessions

</Typography>

<SessionTable

rows={sessions}

onTerminate={async(id:number)=>{

await SecurityService.terminateSession(id);

load();

}}

/>

</Paper>

</Grid>

</Grid>

);

}