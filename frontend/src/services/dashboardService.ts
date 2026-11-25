import api from "./axios";
import type { DashboardData } from "../types/dashboard";

export const DashboardService = {
  async overview(): Promise<DashboardData> {
    const response = await api.get<{ data: DashboardData }>(
      "/dashboard/overview"
    );

    return response.data.data;
  },
};