import { useEffect, useState } from "react";
import {
  Card,
  Grid,
  Typography,
  LinearProgress,
  Box,
} from "@mui/material";

import { DashboardService } from "../services/dashboardService";
import socket from "../services/socket";
import type { DashboardData } from "../types/dashboard";
import PageAnimation from "../components/common/PageAnimation";
import { useAuth } from "../contexts/AuthContext";

const emptyDashboard: DashboardData = {
  summary: {
    total_routers: 0,
    online_routers: 0,
    offline_routers: 0,
    total_networks: 0,
    total_devices: 0,
    connected_devices: 0,
  },

  routers: [],
  networks: [],
  devices: [],
  traffic: [],
};

export default function Dashboard() {
  const [data, setData] = useState<DashboardData>(emptyDashboard);
  const { user } = useAuth();
  const role = user?.role;
  const canViewInfrastructure = role === "admin" || role === "manager" || role === "technician";
  const canViewAnalytics = role === "admin" || role === "manager";

  useEffect(() => {
    loadDashboard();

    const handleDashboardUpdate = (dashboardData: DashboardData) => {
      setData(dashboardData);
    };

    socket.on("dashboard", handleDashboardUpdate);

    return () => {
      socket.off("dashboard", handleDashboardUpdate);
    };
  }, []);

  async function loadDashboard() {
    try {
      const response = await DashboardService.overview();

      setData(response);
    } catch (error) {
      console.error("Failed to load dashboard:", error);
    }
  }

  const summary = data.summary;

  return (
    <PageAnimation>
      <Box sx={{ p: 3 }}>
        <Typography
          variant="h4"
          sx={{ mb: 3, fontWeight: 600 }}
        >
          Dashboard
        </Typography>
        <Typography variant="subtitle1" sx={{ mb: 3 }}>
          {role
            ? `${role.charAt(0).toUpperCase() + role.slice(1)} dashboard`
            : "Dashboard"}
        </Typography>

        <Grid container spacing={3}>

          {role === "viewer" && (
            <Grid size={{ xs: 12 }}>
              <Card sx={{ p: 3 }}>
                <Typography variant="h6">
                  Read-only access
                </Typography>
                <Typography>
                  Your account can view dashboard information but cannot manage network resources.
                </Typography>
              </Card>
            </Grid>
          )}

          {/* TOTAL ROUTERS */}
          {canViewInfrastructure && <>
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Routers
              </Typography>

              <Typography variant="h3">
                {summary.total_routers}
              </Typography>
            </Card>
          </Grid>

          {/* ONLINE ROUTERS */}
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Online Routers
              </Typography>

              <Typography variant="h3">
                {summary.online_routers}
              </Typography>
            </Card>
          </Grid>

          {/* NETWORKS */}
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Networks
              </Typography>

              <Typography variant="h3">
                {summary.total_networks}
              </Typography>
            </Card>
          </Grid>

          {/* DEVICES */}
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Devices
              </Typography>

              <Typography variant="h3">
                {summary.total_devices}
              </Typography>
            </Card>
          </Grid>

          {/* CONNECTED DEVICES */}
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Connected Devices
              </Typography>

              <Typography variant="h3">
                {summary.connected_devices}
              </Typography>
            </Card>
          </Grid>

          {/* OFFLINE ROUTERS */}
          <Grid size={{ xs: 12, sm: 6, md: 3 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Offline Routers
              </Typography>

              <Typography variant="h3">
                {summary.offline_routers}
              </Typography>
            </Card>
          </Grid>
          </>}

          {/* CPU */}
          {canViewAnalytics && <>
          <Grid size={{ xs: 12, md: 6 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                CPU Usage
              </Typography>

              <Box sx={{ mt: 2 }}>
                <LinearProgress
                  variant="determinate"
                  value={getAverageCpu(data)}
                />
              </Box>

              <Typography sx={{ mt: 1 }}>
                {getAverageCpu(data).toFixed(1)}%
              </Typography>
            </Card>
          </Grid>

          {/* MEMORY */}
          <Grid size={{ xs: 12, md: 6 }}>
            <Card sx={{ p: 3 }}>
              <Typography variant="h6">
                Memory Usage
              </Typography>

              <Box sx={{ mt: 2 }}>
                <LinearProgress
                  variant="determinate"
                  value={getAverageMemory(data)}
                />
              </Box>

              <Typography sx={{ mt: 1 }}>
                {getAverageMemory(data).toFixed(1)}%
              </Typography>
            </Card>
          </Grid>
          </>}

        </Grid>
      </Box>
    </PageAnimation>
  );
}


/**
 * Calculate average CPU usage
 * from the routers returned by the backend.
 */
function getAverageCpu(data: DashboardData): number {
  if (!data.routers || data.routers.length === 0) {
    return 0;
  }

  const total = data.routers.reduce(
    (sum, router) => sum + (router.cpu_usage || 0),
    0
  );

  return Math.min(total / data.routers.length, 100);
}


/**
 * Calculate average memory usage
 * from the routers returned by the backend.
 */
function getAverageMemory(data: DashboardData): number {
  if (!data.routers || data.routers.length === 0) {
    return 0;
  }

  const total = data.routers.reduce(
    (sum, router) => sum + (router.memory_usage || 0),
    0
  );

  return Math.min(total / data.routers.length, 100);
}