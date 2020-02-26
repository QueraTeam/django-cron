
Summary of my fork changes
==========================
### Access to change CronJobManager from django settings (optional)

```python
CRON_MANAGER = 'path.to.custom.MyManager'
```

---
### Add day config to CronJob schedule

- Indexes start from zero.
- Any value (default): `'*'`
- Cron format:
    - comma separated values: `'0,2,5'`
    - step: `'*/3'` (=0,3,6,9,...)  , `'*/2+1'` (=1,3,5,...)
    - range: `'5-10'` (=5,6,...,10)

- List of `False/True` or `0/1`: [0, 0, 1, 0, 0, 1, ...]

```python
day_of_month='*',  # 0-30
month_numbers='*',  # 0-11
day_of_week='*',  # 0-6 (Sunday=0 ... Saturday=6)
```

Example:

```python
from django_cron import CronJobBase, Schedule

class ExampleCronJob(CronJobBase):
    RUN_AT_TIMES = ['10:10', '22:10']
    schedule = Schedule(run_at_times=RUN_AT_TIMES, day_of_week='2')
    code = 'cron.ExampleCronJob'
    def do(self):
        pass
```

---
### Add a method to CronJob for get run times in future
- Parameters: `from_datetime`, `to_datetime`


---
## Move `should_run_now` method to CronJob to override it if required.

Example:

```python
from django_cron import CronJobBase, Schedule
from datetime import datetime


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

```
