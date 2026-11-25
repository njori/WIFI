import api from "../api/api";

const BASE="/security";

export const SecurityService={

    async dashboard(){

        const res=await api.get(`${BASE}/dashboard`);

        return res.data;

    },

    async auditLogs(){

        const res=await api.get(`${BASE}/audit`);

        return res.data;

    },

    async roles(){

        const res=await api.get(`${BASE}/roles`);

        return res.data;

    },

    async sessions(){

        const res=await api.get(`${BASE}/sessions`);

        return res.data;

    },

    async terminateSession(id:number){

        await api.delete(`${BASE}/sessions/${id}`);

    }

};