import api from "../api/api";

const BASE="/settings";

export const SettingsService={

    async get(){

        const res=await api.get(BASE);

        return res.data;

    },

    async save(data:any){

        const res=await api.put(BASE,data);

        return res.data;

    },

    async backup(){

        return await api.post(`${BASE}/backup`);

    },

    async restore(){

        return await api.post(`${BASE}/restore`);

    }

};