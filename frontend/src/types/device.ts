export interface Device{

    id:number;

    hostname:string;

    ip_address:string;

    mac_address:string;

    manufacturer:string;

    operating_system:string;

    device_type:string;

    signal_strength:number;

    router_id:number;

    router_name?:string;

    is_connected:boolean;

    last_seen:string;

}