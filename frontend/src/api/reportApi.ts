import api from "./axios";

export const ReportApi = {

    dashboard() {
        return api.get("/reports/dashboard");
    },

    history() {
        return api.get("/reports/history");
    },

    available() {
        return api.get("/reports/available");
    },

    generatePDF() {
        return api.post("/reports/pdf");
    },

    generateExcel() {
        return api.post("/reports/excel");
    },

    generateCSV() {
        return api.post("/reports/csv");
    },

    generateJSON() {
        return api.post("/reports/json");
    },

    download(filename: string) {
        return api.get(`/reports/download/${filename}`, {
            responseType: "blob"
        });
    }

};