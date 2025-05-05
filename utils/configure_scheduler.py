from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

def configure_scheduler():
    jobstores = {
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite'),
    }
    job_defaults = {
        "replace_existing": True
    }
    return AsyncIOScheduler(jobstores=jobstores, job_defaults=job_defaults)