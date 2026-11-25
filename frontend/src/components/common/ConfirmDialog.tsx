import {

Dialog,

DialogTitle,

DialogActions,

Button

} from "@mui/material";

export default function ConfirmDialog({

open,

message,

onYes,

onNo

}:any){

return(

<Dialog open={open}>

<DialogTitle>

{message}

</DialogTitle>

<DialogActions>

<Button

onClick={onNo}

>

Cancel

</Button>

<Button

color="error"

onClick={onYes}

>

Confirm

</Button>

</DialogActions>

</Dialog>

);

}