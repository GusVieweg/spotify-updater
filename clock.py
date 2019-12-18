from apscheduler.schedulers.blocking import BlockingScheduler
from SpotifyTools import SpotifyUpdater

sched = BlockingScheduler()


@sched.scheduled_job('interval', days=14, start_date='2019-12-19 00:01:00')
def scheduled_job():
    su = SpotifyUpdater()
    su.update_feature_song()


sched.start()
