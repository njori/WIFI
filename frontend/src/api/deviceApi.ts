import api from "./axios";

export const DeviceApi = {

    all() {
        return api.get("/devices");
    },

    get(id: number) {
        return api.get(`/devices/${id}`);
    },

    create(data: any) {
        return api.post("/devices", data);
    },

    update(id: number, data: any) {
        return api.put(`/devices/${id}`, data);
    },

    delete(id: number) {
        return api.delete(`/devices/${id}`);
    },

    disconnect(id: number) {
        return api.post(`/devices/${id}/disconnect`);
    },

    reconnect(id: number) {
        return api.post(`/devices/${id}/reconnect`);
    },

    history(id: number) {
        return api.get(`/devices/${id}/history`);
    }

};