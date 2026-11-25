import { useEffect } from "react";

import socket from "../services/socket";

export default function useSocket(

event:string,

callback:any

){

useEffect(()=>{

socket.on(

event,

callback

);

return()=>{

socket.off(

event,

callback

);

};

},[event]);

}