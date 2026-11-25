import {

LineChart,
Line,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer

} from "recharts";

export default function CpuChart({data}:any){

return(

<ResponsiveContainer width="100%" height={300}>

<LineChart data={data}>

<XAxis dataKey="time"/>

<YAxis/>

<Tooltip/>

<Line

type="monotone"

dataKey="cpu"

/>

</LineChart>

</ResponsiveContainer>

);

}