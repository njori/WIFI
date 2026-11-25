import { Badge } from "@mui/material";
import NotificationsIcon from "@mui/icons-material/Notifications";

export default function NotificationBadge({

count

}:{

count:number

}){

return(

<Badge

badgeContent={count}

color="error"

>

<NotificationsIcon/>

</Badge>

);

}