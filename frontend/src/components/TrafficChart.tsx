import {

BarChart,
Bar,
XAxis,
YAxis,
Tooltip,
ResponsiveContainer

} from "recharts";

export default function TrafficChart({data}:any){

return(

<ResponsiveContainer width="100%" height={300}>

<BarChart data={data}>

<XAxis dataKey="time"/>

<YAxis/>

<Tooltip/>

<Bar dataKey="upload"/>

<Bar dataKey="download"/>

</BarChart>

</ResponsiveContainer>

);

}