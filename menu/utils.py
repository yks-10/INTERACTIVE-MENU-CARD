import logging
import sys

from rest_framework import status
from rest_framework.response import Response
from validators.Errorcode import ErrorCode
from validators.Errormessage import ErrorMessage


class CommonUtils(object):

    @staticmethod
    def dispatch_success(request, response, code=status.HTTP_200_OK):
        """
        :param request: request object
        :param response: response object
        :param code: 200 - success code
        :return: json object
        """

        response = {"status": "success", "result": response}

        # logging the success response
        extras = {
            "status": "Success",
            "url": request.get_full_path(),
            "log_message": "Request completed!",
            "method": request.method,
            "user": request.user
        }
        logger = logging.getLogger('success')
        logger.setLevel(logging.INFO)
        logger.info("Success: ", extra=extras)

        return Response(response, status=code)

    @staticmethod
    def dispatch_failure(request, identifier, response=None, code=status.HTTP_400_BAD_REQUEST, message_params=None):
        """
        @param request: request object
        @param identifier: error identifier code
        @param response: response object may be empty in some cases
        @param code: 400 - Failure
        @param message_params: To add in error message
        :return: json object
        """
        try:
            if hasattr(ErrorCode, identifier):
                error_code = getattr(ErrorCode, identifier)
            else:
                error_code = code
            error_message = getattr(ErrorMessage, identifier)
            if error_message and message_params:
                error_message = error_message.format(**message_params)
            errors = {}
            if response is None:
                errors['status'] = 'failed'
                errors['code'] = error_code
                errors['message'] = error_message
            else:
                errors['status'] = 'failed'
                errors['code'] = error_code
                errors['message'] = error_message
                errors['errors'] = response

            response = Response(data=errors, status=code)

            # logging the failure response
            extras = {
                "request_data": request.data,
                "response_data": str(response.data),
                "status": "Failed",
                "url": request.get_full_path(),
                "log_message": error_message,
                "method": request.method,
                "user": request.user,
                "file_name": '',
                "line_no": ''
            }
            exception_type, exception_object, exception_traceback = sys.exc_info()
            if exception_type and exception_object and exception_traceback:
                extras["file_name"] = exception_traceback.tb_frame.f_code.co_filename
                extras["line_no"] = exception_traceback.tb_lineno

            logger = logging.getLogger('failure')
            logger.setLevel(logging.DEBUG)
            logger.debug("Error: ", extra=extras)

            return response
        except Exception as e:
            print(str(e))

