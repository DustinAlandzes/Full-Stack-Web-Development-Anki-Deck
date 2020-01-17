import logging
import os

from apscheduler.schedulers.blocking import BlockingScheduler

from fetch_assignments_create_issues import create_issues_for_assignments

if __name__ == "__main__":
    logging.basicConfig(filename='bootcampspot-homework-grading.log', level=logging.DEBUG)

    scheduler = BlockingScheduler()
    scheduler.add_job(create_issues_for_assignments, 'interval', hours=1)

    # from https://github.com/agronholm/apscheduler/blob/master/examples/schedulers/blocking.py
    try:
        print("Running create_issues_for_assignments, and then starting a scheduler to run it again every hour")
        create_issues_for_assignments()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass
    except Exception as e:
        logging.debug(repr(e))
