import api from "../api/api";

const BASE="/reports";

export const ReportService={

    async history(){

        const res=await api.get(`${BASE}/history`);

        return res.data;

    },

    async available(){

        const res=await api.get(`${BASE}/available`);

        return res.data;

    },

    async generatePDF(){

        return await api.post(`${BASE}/pdf`);

    },

    async generateExcel(){

        return await api.post(`${BASE}/excel`);

    },

    async generateCSV(){

        return await api.post(`${BASE}/csv`);

    },

    async generateJSON(){

        return await api.post(`${BASE}/json`);

    },

    async delete(name:string){

        return await api.delete(

            `${BASE}/${name}`

        );

    }

};