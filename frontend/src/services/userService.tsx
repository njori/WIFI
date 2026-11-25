import api from "../api/api";

const BASE="/users";

export const UserService={

    async getAll(){

        const res=await api.get(BASE);

        return res.data.data;

    },

    async create(data:any){

        const res=await api.post(BASE,data);

        return res.data;

    },

    async update(id:number,data:any){

        const res=await api.put(`${BASE}/${id}`,data);

        return res.data.data;

    },

    async remove(id:number){

        await api.delete(`${BASE}/${id}`);

    },

    async resetPassword(id:number){

        await api.post(`${BASE}/${id}/reset-password`);

    },

    async toggleStatus(id:number){

        await api.put(`${BASE}/${id}/status`);

    },

    async history(id:number){

        const res=await api.get(`${BASE}/${id}/history`);

        return res.data;

    }

};