export interface Notification{

    id:number;

    title:string;

    message:string;

    level:"info"|"warning"|"error"|"success";

    is_read:boolean;

    created_at:string;

}