# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_recognize_receipts.py

DESCRIPTION:
    This sample demonstrates how to analyze receipts from both a file and a url.

USAGE:
    python sample_recognize_receipts.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer subscription key
"""

import os


class RecognizeReceiptsSample(object):

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]

    def recognize_receipts_from_file(self):
        # TODO: this can be used as examples in sphinx
        print("=========Recognize Receipts from a file=========")
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer import FormRecognizerClient
        form_recognizer_client = FormRecognizerClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key))
        with open("sample_forms/receipt/contoso-allinone.jpg", "rb") as f:
            poller = form_recognizer_client.begin_recognize_receipts(stream=f.read())
        receipts = poller.result()

        for idx, receipt in enumerate(receipts):
            print("--------Recognizing receipt #{}--------".format(idx))
            print("Total: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.total.value,
                receipt.total.confidence,
                receipt.total.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.total.value_data.bounding_box]),
            ))
            print("Merchant: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.merchant_name.value,
                receipt.merchant_name.confidence,
                receipt.merchant_name.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.merchant_name.value_data.bounding_box]),
            ))
            print("Transaction date: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.transaction_date.value,
                receipt.transaction_date.confidence,
                receipt.transaction_date.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.transaction_date.value_data.bounding_box]),
            ))
            print("--------------------------------------")
        print("===============================================")

    def recognize_receipts_from_url(self):
        # TODO: this can be used as examples in sphinx
        print("=========Recognize Receipts from a URL=========")
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer import FormRecognizerClient
        form_recognizer_client = FormRecognizerClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key))
        poller = form_recognizer_client.begin_recognize_receipts_from_url(
            url="https://raw.githubusercontent.com/Azure/azure-sdk-for-python/master/sdk/formrecognizer/azure-ai-formrecognizer/tests/sample_forms/receipt/contoso-receipt.png"
        )
        receipts = poller.result()

        for idx, receipt in enumerate(receipts):
            print("--------Recognizing receipt #{}--------".format(idx))
            print("Total: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.total.value,
                receipt.total.confidence,
                receipt.total.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.total.value_data.bounding_box]),
            ))
            print("Merchant: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.merchant_name.value,
                receipt.merchant_name.confidence,
                receipt.merchant_name.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.merchant_name.value_data.bounding_box]),
            ))
            print("Transaction date: {} (Confidence score of {}, based on text value '{}', with bounding box {})".format(
                receipt.transaction_date.value,
                receipt.transaction_date.confidence,
                receipt.transaction_date.value_data.text,
                ", ".join([ "[{}, {}]".format(p.x, p.y) for p in receipt.transaction_date.value_data.bounding_box]),
            ))
            print("--------------------------------------")
        print("===============================================")



if __name__ == '__main__':
    sample = RecognizeReceiptsSample()
    sample.recognize_receipts_from_file()
    sample.recognize_receipts_from_url()

