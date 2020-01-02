from apscheduler.schedulers.blocking import BlockingScheduler
from SpotifyTools import SpotifyUpdater

sched = BlockingScheduler()


@sched.scheduled_job('interval', days=14, start_date='2020-01-02 12:20:00', timezone="US/Eastern")
def scheduled_job():
    su = SpotifyUpdater()
    print("Initialized Spotify Updater.")
    su.update_feature_song()
    print("Feature song updated.")


sched.start()
