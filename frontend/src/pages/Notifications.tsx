import {

useEffect,

useState

} from "react";

import NotificationCard from "../components/NotificationCard";

import socket from "../services/socket";

import {

NotificationService

} from "../services/notificationService";

export default function Notifications(){

const[data,setData]=useState<any[]>([]);

async function load(){

const result=

await NotificationService.getAll();

setData(result);

}

useEffect(()=>{

load();

socket.on(

"notification",

(notification)=>{

setData(prev=>[

notification,

...prev

]);

}

);

return()=>{

socket.off("notification");

};

},[]);

return(

<div>

<h2>

Notifications

</h2>

{

data.map(item=>(

<NotificationCard

key={item.id}

notification={item}

onRead={async(id:number)=>{

await NotificationService.markRead(id);

load();

}}

onDelete={async(id:number)=>{

await NotificationService.delete(id);

load();

}}

/>

))

}

</div>

);

}