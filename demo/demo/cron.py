import logging
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

from django_cron import CronJobBase, Schedule


def send_mail(subject, message, from_email, recipient_emails):
    try:
        email = EmailMessage(subject, message, from_email, recipient_emails)
        email.send()
    except Exception as e:
        logging.error(
            f'Error sending message [{subject}] from {from_email} to {recipient_emails} {e}'
        )


class EmailUserCountCronJob(CronJobBase):
    """
    Send an email with the user count.
    """
    RUN_EVERY_MINS = 0 if settings.DEBUG else 360  # 6 hours when not DEBUG

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'cron.EmailUsercountCronJob'

    def do(self):
        message = f'Active users: {User.objects.count()}'
        print(message)
        send_mail(
            '[django-cron demo] Active user count',
            message,
            'no-reply@django-cron-demo.com',
            ['test@django-cron-demo.com']
        )


class EmailUserCountCronJob2(CronJobBase):
    """
    Send an email with the user count.
    """
    RUN_AT_TIMES = ['10:10', '22:10']

    schedule = Schedule(run_at_times=RUN_AT_TIMES, day_of_week='2')
    code = 'cron.EmailUsercountCronJob'

    def do(self):
        message = f'Active users: {User.objects.count()}'
        print(message)
        send_mail(
            '[django-cron demo] Active user count',
            message,
            'no-reply@django-cron-demo.com',
            ['test@django-cron-demo.com']
        )


class TestCronJob(CronJobBase):
    RUN_AT_TIMES = ['10:10', '22:10']
    schedule = Schedule(
        run_at_times=RUN_AT_TIMES,
        # day_of_week='*/2',
    )

    code = 'demo.TestCronJob'

    def do(self):
        print('do TestCronJob')
        return f'do TestCronJob at {datetime.now()}'

    def should_run_now(self, force=False):
        print('override should_run_now in cron job')
        '''
        if some_conditions_to_avoid_run_job:
            return False
        '''
        return super(TestCronJob, self).should_run_now(force=force)
