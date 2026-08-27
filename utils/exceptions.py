class DevTrackError(Exception):
    """Base exception for DevTrack."""
    pass


class TaskAlreadyCompletedError(DevTrackError):
    """Raised when an already completed task is completed again."""
    pass