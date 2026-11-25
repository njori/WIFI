import api from "./axios";

export const UserApi = {

    all() {
        return api.get("/users");
    },

    get(id: number) {
        return api.get(`/users/${id}`);
    },

    create(data: any) {
        return api.post("/users", data);
    },

    update(id: number, data: any) {
        return api.put(`/users/${id}`, data);
    },

    delete(id: number) {
        return api.delete(`/users/${id}`);
    },

    resetPassword(id: number) {
        return api.post(`/users/${id}/reset-password`);
    },

    toggleStatus(id: number) {
        return api.put(`/users/${id}/status`);
    },

    loginHistory(id: number) {
        return api.get(`/users/${id}/history`);
    },

    profile() {
        return api.get("/users/profile");
    }

};