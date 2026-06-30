from django.utils.translation import gettext as _
from django.template.defaultfilters import pluralize


def humanize_duration(duration):
    """
    Returns a humanized string representing time difference

    For example: 2 days 1 hour 25 minutes 10 seconds
    """
    days = duration.days
    hours = int(duration.seconds / 3600)
    minutes = int(duration.seconds % 3600 / 60)
    seconds = int(duration.seconds % 3600 % 60)

    parts = []
    if days > 0:
        parts.append(f"{days} {pluralize(days, _('day,days'))}")

    if hours > 0:
        parts.append(f"{hours} {pluralize(hours, _('hour,hours'))}")

    if minutes > 0:
        parts.append(f"{minutes} {pluralize(minutes, _('minute,minutes'))}")

    if seconds > 0:
        parts.append(f"{seconds} {pluralize(seconds, _('second,seconds'))}")

    return ', '.join(parts) if len(parts) != 0 else _('< 1 second')
