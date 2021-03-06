""" Copyright start
  Copyright (C) 2008 - 2022 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from connectors.core.connector import Connector, get_logger, ConnectorError
from .operations import _check_health, _run_operation

logger = get_logger('ocr-space')


class OCRSpace(Connector):

    def execute(self, config, operation, params, **kwargs):
        try:
            logger.info('ocr-space: Executing {} operation'.format(operation))
            params.update({"operation": operation})
            return _run_operation(config, params)
        except Exception as err:
            logger.error('ocr-space: {}'.format(err))
            raise ConnectorError('ocr-space: {}'.format(err))

    def check_health(self, config):
        return _check_health(config)
