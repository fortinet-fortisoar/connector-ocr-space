""" Copyright start
  Copyright (C) 2008 - 2021 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

import requests
import subprocess

from connectors.cyops_utilities.builtins import download_file_from_cyops
from integrations.crudhub import make_request
from connectors.core.connector import get_logger, ConnectorError
from os.path import join

logger = get_logger('ocr-space')


class OCRSpace(object):
    def __init__(self, config):
        self.log = logger
        self.maximum_file_size = 32000000
        self.base_url = config.get('server').strip() + '/Parse/Image'
        if not self.base_url.startswith('https://'):
            self.base_url = 'https://' + self.base_url
        self.api_key = config.get('api_key')
        self.verify_ssl = config.get('verify_ssl')
        self.payload = {'isOverlayRequired': 'True', 'apikey': self.api_key, 'language': 'eng'}
        self.__setupSession()

    def __setupSession(self):
        self.log.info('Setup session')
        self.session = requests.Session()
        self.session.verify = self.verify_ssl
        self.session.headers.update({'accept': 'application/json'})

    def __postUrl(self, params={}, data={}, files=None):
        try:
            self.log.info('Params: {}'.format(params))
            if files is not None:
                self.log.info('Posting files.')
            if data:
                self.log.info('Posting data.')
                self.payload.update(data)
            url = self.base_url
            self.log.info('Posting to URL: {}'.format(url))
            res = self.session.post(url, params=params, data=self.payload, files=files)
            if res.status_code == 204:
                return {'message': 'Request rate limit exceeded. You are making more requests than allowed.'}
            return res.json()
        except Exception as Err:
            raise ConnectorError(Err)

    def submitFile(self, file_iri, data):
        try:
            file_path = join('/tmp', download_file_from_cyops(file_iri)['cyops_file_path'])
            logger.info(file_path)
            out = subprocess.Popen(["file", str(file_path)], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            stdout,stderr = out.communicate()
            file_type = {'filetype': str(stdout).split(' ')[1]}
            data.update(file_type)
            with open(file_path, 'rb') as attachment:
                file_data = attachment.read()
            if file_data:
                files = {'file': file_data}
                res = self.__postUrl(data=data, files=files)
                return res
            raise ConnectorError('File size too large, submit file up to 32 MB')
        except Exception as Err:
            logger.error('Error in submitFile(): %s' % Err)
            logger.exception('Error in submitFile(): %s' % Err)
            raise ConnectorError('Error in submitFile(): %s' % Err)

    def scanUrlBase64(self, data):
        try:
            self.log.info('Get URL/Base64 image report.')
            response = self.__postUrl(data=data)
            return response
        except Exception as Err:
            logger.exception('Error in getUrlReport(): %s' % Err)
            raise ConnectorError('Error in getUrlReport(): %s' % Err)

    def handle_params(self, params):
        value = str(params.get('value'))
        input_type = params.get('input')
        try:
            if isinstance(value, bytes):
                value = value.decode('utf-8')
            if input_type == 'Attachment ID':
                if not value.startswith('/api/3/attachments/'):
                    value = '/api/3/attachments/{0}'.format(value)
                attachment_data = make_request(value, 'GET')
                file_iri = attachment_data['file']['@id']
                file_name = attachment_data['file']['filename']
                logger.info('file id = {0}, file_name = {1}'.format(file_iri, file_name))
                return file_iri
            elif input_type == 'File IRI':
                if value.startswith('/api/3/files/'):
                    return value
                else:
                    raise ConnectorError('Invalid File IRI {0}'.format(value))
        except Exception as err:
            logger.info('handle_params(): Exception occurred {0}'.format(err))
            raise ConnectorError('Requested resource could not be found with input type "{0}" and value "{1}"'.format(input_type, value.replace('/api/3/attachments/', '')))

    def parse_image(self, params):
        i_url = params.get('image_url')
        f_val = params.get('value')
        base64 = params.get('base64_image')
        f_type = params.get('file_type')
        data = {}
        if i_url:
            data = {'url': i_url}
        elif base64:
            data = {'base64Image': "data:image/{};base64,{}".format(f_type, base64)}
        elif f_val:
            file_iri = self.handle_params(params)
            return self.submitFile(file_iri, data)
        return self.scanUrlBase64(data)


def _run_operation(config, params):
    operation = params['operation']
    ocr_object = OCRSpace(config)
    command = getattr(OCRSpace, operation)
    response = command(ocr_object, params)
    return response


def _check_health(config):
    try:
        url = 'https://ocr.space/Content/Images/ocr.space.logo.png'
        ocs = OCRSpace(config)
        res = ocs.scanUrlBase64({'url': url})
        if res:
            return True
    except Exception as Err:
        raise ConnectorError('Invalid URL or Credentials')
