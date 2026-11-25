import {

createContext,

useState

} from "react";

export const NotificationContext=

createContext<any>(null);

export function NotificationProvider({

children

}:any){

const[message,setMessage]=

useState("");

return(

<NotificationContext.Provider

value={{

message,

setMessage

}}

>

{children}

</NotificationContext.Provider>

);

}