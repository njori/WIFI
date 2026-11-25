export interface AuditLog{

    id:number;

    username:string;

    action:string;

    ip_address:string;

    created_at:string;

}

export interface Session{

    id:number;

    username:string;

    ip_address:string;

    login_time:string;

    active:boolean;

}

export interface Role{

    id:number;

    name:string;

    description:string;

    permissions:string[];

}