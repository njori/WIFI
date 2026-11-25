from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()


def register_jobs(app):

    from app.services.discovery_service import DiscoveryService
    from app.services.monitoring_service import MonitoringService
    from app.services.scheduled_report_service import ScheduledReportService

    # Device Discovery
    scheduler.add_job(
        lambda: run_with_context(app, DiscoveryService.scan),
        trigger="interval",
        minutes=1,
        id="device_discovery",
        replace_existing=True
    )

    # Router Monitoring
    scheduler.add_job(
        lambda: run_with_context(app, MonitoringService.monitor),
        trigger="interval",
        seconds=30,
        id="router_monitor",
        replace_existing=True
    )

    # Daily Report
    scheduler.add_job(
        lambda: run_with_context(app, ScheduledReportService.daily),
        trigger="cron",
        hour=18,
        minute=0,
        id="daily_report",
        replace_existing=True
    )

    # Weekly Report
    scheduler.add_job(
        lambda: run_with_context(app, ScheduledReportService.weekly),
        trigger="cron",
        day_of_week="sun",
        hour=18,
        minute=0,
        id="weekly_report",
        replace_existing=True
    )

    # Monthly Report
    scheduler.add_job(
        lambda: run_with_context(app, ScheduledReportService.monthly),
        trigger="cron",
        day=1,
        hour=18,
        minute=0,
        id="monthly_report",
        replace_existing=True
    )

    # Cleanup
    scheduler.add_job(
        lambda: run_with_context(app, ScheduledReportService.cleanup),
        trigger="cron",
        hour=3,
        minute=0,
        id="cleanup_reports",
        replace_existing=True
    )


def run_with_context(app, job):
    with app.app_context():
        job()


def start_scheduler(app):

    if scheduler.running:
        return

    register_jobs(app)

    scheduler.start()

    print("Scheduler started successfully.")