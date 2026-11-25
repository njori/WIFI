export interface DashboardData {
  summary: {
    total_routers: number;
    online_routers: number;
    offline_routers: number;
    total_networks: number;
    total_devices: number;
    connected_devices: number;
  };

  routers?: {
    id: number;
    name: string;
    ip_address: string;
    cpu_usage: number;
    memory_usage: number;
    is_online: boolean;
  }[];

  networks?: {
    id: number;
    ssid: string;
    router_id: number;
    channel?: number;
    band?: string;
    vlan?: number;
    device_count?: number;
  }[];

  devices?: {
    id: number;
    hostname?: string;
    ip_address?: string;
    mac_address?: string;
    device_type?: string;
    is_connected?: boolean;
  }[];

  traffic?: {
    router_id: number;
    interface: string;
    upload: number;
    download: number;
    utilization: number;
    created_at: string;
  }[];

  [key: string]: unknown;
}