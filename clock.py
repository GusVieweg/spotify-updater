from apscheduler.schedulers.blocking import BlockingScheduler
from SpotifyTools import SpotifyUpdater

sched = BlockingScheduler()


@sched.scheduled_job('interval', days=14, start_date='2020-01-02 11:25:00', timezone="US/Eastern")
def scheduled_job():
    su = SpotifyUpdater()
    su.update_feature_song()


sched.start()
