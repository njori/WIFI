import {

AreaChart,
Area,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer

} from "recharts";

export default function MemoryChart({data}:any){

return(

<ResponsiveContainer width="100%" height={300}>

<AreaChart data={data}>

<XAxis dataKey="time"/>

<YAxis/>

<Tooltip/>

<Area

type="monotone"

dataKey="memory"

/>

</AreaChart>

</ResponsiveContainer>

);

}