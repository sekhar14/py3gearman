"""
Gearman API - Client, worker, and admin client interfaces
"""

__version__ = '2.0.2'

from py3gearman.admin_client import GearmanAdminClient
from py3gearman.client import GearmanClient
from py3gearman.worker import GearmanWorker

from py3gearman.connection_manager import DataEncoder
from py3gearman.constants import PRIORITY_NONE, PRIORITY_LOW, PRIORITY_HIGH, JOB_PENDING, JOB_CREATED, JOB_FAILED, JOB_COMPLETE

import logging

class NullHandler(logging.Handler):
    def emit(self, record):
        pass

gearman_root_logger = logging.getLogger('py3gearman')
gearman_root_logger.addHandler(NullHandler())