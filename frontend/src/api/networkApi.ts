import api from "./axios";

export const NetworkApi = {

    all() {
        return api.get("/networks");
    },

    get(id: number) {
        return api.get(`/networks/${id}`);
    },

    create(data: any) {
        return api.post("/networks", data);
    },

    update(id: number, data: any) {
        return api.put(`/networks/${id}`, data);
    },

    delete(id: number) {
        return api.delete(`/networks/${id}`);
    },

    scan() {
        return api.post("/networks/scan");
    },

    statistics() {
        return api.get("/networks/statistics");
    }

};