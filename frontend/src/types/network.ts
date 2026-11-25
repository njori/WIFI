export interface Network {

    id:number;

    name:string;

    cidr:string;

    gateway:string;

    subnet_mask:string;

    vlan:number;

    dns_server:string;

    description:string;

    router_id:number;

    router_name?:string;

}