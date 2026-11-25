import api from "./axios";

export const NotificationApi = {

    all() {
        return api.get("/notifications");
    },

    unread() {
        return api.get("/notifications/unread");
    },

    markRead(id: number) {
        return api.put(`/notifications/${id}/read`);
    },

    markAllRead() {
        return api.put("/notifications/read-all");
    },

    delete(id: number) {
        return api.delete(`/notifications/${id}`);
    },

    clear() {
        return api.delete("/notifications");
    }

};