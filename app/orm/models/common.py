"""
Common ORM classes
=====================

"""

import logging
import os

from sqlalchemy import Column, text
from sqlalchemy.dialects.mysql import BIGINT, TIMESTAMP, VARCHAR
from sqlalchemy.sql.functions import now

__author__ = "vishalkumar9565@gmail.com"

_LOGGER_PATH = os.path.join("config", "logging.json")
LOGGER = logging.getLogger(__name__)


class BaseClass(object):
    version_id = Column(BIGINT(unsigned=True), nullable=False)
    # created_by = Column(VARCHAR(255), nullable=False, default="SYSTEM", server_default="SYSTEM")

    created_on = Column(TIMESTAMP, nullable=False, server_default=now())

    last_updated_on = Column(TIMESTAMP, nullable=True,
                             server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

    last_updated_by = Column(VARCHAR(255), nullable=True, default="SYSTEM", server_default="SYSTEM")

    # Version identifier
    __mapper_args__ = {
        "version_id_col": version_id
    }

    def _asdict(self):
        result = dict()
        for key in self.__mapper__.c.keys():
            try:
                result[key] = [new_obj._asdict() for new_obj in getattr(self, key)]
            except:
                result[key] = getattr(self, key)
        return result
