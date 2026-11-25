import {

Dialog,
DialogTitle,
DialogContent,
List,
ListItem,
ListItemText

} from "@mui/material";

export default function LoginHistoryDialog({

open,
history,
onClose

}:any){

return(

<Dialog

open={open}

onClose={onClose}

fullWidth

>

<DialogTitle>

Login History

</DialogTitle>

<DialogContent>

<List>

{

history.map((item:any,index:number)=>(

<ListItem key={index}>

<ListItemText

primary={item.ip_address}

secondary={item.login_time}

/>

</ListItem>

))

}

</List>

</DialogContent>

</Dialog>

);

}