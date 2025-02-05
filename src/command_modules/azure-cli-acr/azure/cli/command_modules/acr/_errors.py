# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

# pylint: disable=line-too-long


class ErrorClass:
    error_title = ""
    error_message = ""

    def __init__(self, title, message):
        self.error_title = title
        self.error_message = message

    def get_error_message(self, additional_message=None):
        if additional_message:
            return "An error occurred: {}\n{}\n{}".format(self.error_title, self.error_message, additional_message)

        return "An error occurred: {}\n{}".format(self.error_title, self.error_message)

    def set_error_message(self, message):
        return ErrorClass(self.error_title, message)

    def append_error_message(self, message):
        return self.set_error_message(self.error_message + "\n" + message)

    def format_error_message(self, *args):
        return self.set_error_message(self.error_message.format(*args))


# DOCKER ERRORS
DOCKER_COMMAND_ERROR = ErrorClass(
    "DOCKER_COMMAND_ERROR",
    "Please verify if Docker client is installed and running."
)


DOCKER_DAEMON_ERROR = ErrorClass(
    "DOCKER_DAEMON_ERROR",
    "Please verify if Docker daemon is running, or try restarting it."
)


DOCKER_VERSION_ERROR = ErrorClass(
    "DOCKER_VERSION_ERROR",
    "An error occured while retrieving Docker version. Please try verifying it manually."
)


DOCKER_PULL_ERROR = ErrorClass(
    "DOCKER_PULL_ERROR",
    "An error occurred while pulling a sample image. Please validate your network connection and verify if docker daemon is running properly."
)


# HELM ERRORS
HELM_COMMAND_ERROR = ErrorClass(
    "HELM_COMMAND_ERROR",
    "Please verify if Helm is installed."
)

HELM_VERSION_ERROR = ErrorClass(
    "HELM_VERSION_ERROR",
    "An error occurred while retrieving Helm version. Please make sure that you have the latest Azure CLI version, and that you are using the recommended Helm version."
)


# CONNECTIVITY ERRORS
CONNECTIVITY_DNS_ERROR = ErrorClass(
    "CONNECTIVITY_DNS_ERROR",
    "Failed to reach DNS for registry '{}'. Please check if the spelling is correct, if the CLI environment is on correct cloud and your network connectivity."
)


CONNECTIVITY_FORBIDDEN_ERROR = ErrorClass(
    "CONNECTIVITY_FORBIDDEN_ERROR",
    "Looks like you don't have access to registry '{}'. Are firewalls and virtual networks enabled?"
)


CONNECTIVITY_CHALLENGE_ERROR = ErrorClass(
    "CONNECTIVITY_CHALLENGE_ERROR",
    "Registry '{}' did not issue a challenge."
)


CONNECTIVITY_AAD_LOGIN_ERROR = ErrorClass(
    "CONNECTIVITY_AAD_LOGIN_ERROR",
    "Registry '{}' does not support AAD login."
)


CONNECTIVITY_REFRESH_TOKEN_ERROR = ErrorClass(
    "CONNECTIVITY_REFRESH_TOKEN_ERROR",
    "Access to registry '{}' was denied. Response code: {}. Please try running 'az login' again to refresh permissions."
)


CONNECTIVITY_ACCESS_TOKEN_ERROR = ErrorClass(
    "CONNECTIVITY_ACCESS_TOKEN_ERROR",
    "Access to registry '{}' was denied. Response code: {}. Please try running 'az login' again to refresh permissions."
)


# GENERAL ERRORS
LOGIN_SERVER_ERROR = ErrorClass(
    "LOGIN_SERVER_ERROR",
    "An error occurred while retrieving the login server for registry '{}'. Please check if the spelling is correct, if the CLI environment is on correct cloud and if you have the right permissions on it."
)


UNEXPECTED_ERROR = ErrorClass(
    "UNEXPECTED_ERROR",
    "An unexpected error occurred."
)
