# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_recognize_content_from_url.py

DESCRIPTION:
    This sample demonstrates how to extact text and layout information a document
    given through a URL.
USAGE:
    python sample_recognize_content_from_url.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer subscription key
"""

import os


class RecognizeContentFromURLSample(object):

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]

    def recognize_content_from_url(self):
        # TODO: this can be used as examples in sphinx
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer import FormRecognizerClient
        form_recognizer_client = FormRecognizerClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key))
        poller = form_recognizer_client.begin_recognize_content_from_url(
            url="https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/forms/Invoice_1.pdf"
        )
        contents = poller.result()

        for idx, content in enumerate(contents):
            print("--------Recognizing content #{}--------".format(idx))
            print("Has width: {} and height: {}, measured with unit: {}".format(
                content.width,
                content.height,
                content.unit
            ))
            print("--------------------------------------")


if __name__ == '__main__':
    sample = RecognizeContentFromURLSample()
    sample.recognize_content_from_url()
