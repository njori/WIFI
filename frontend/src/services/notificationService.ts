import api from "../api/api";

const BASE="/notifications";

export const NotificationService={

    async getAll(){

        const res=await api.get(BASE);

        return res.data;

    },

    async markRead(id:number){

        await api.put(`${BASE}/${id}/read`);

    },

    async delete(id:number){

        await api.delete(`${BASE}/${id}`);

    }

};