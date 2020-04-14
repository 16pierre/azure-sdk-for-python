# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_differentiate_custom_forms_with_labeled_and_unlabeled_models_async.py

DESCRIPTION:
    This sample demonstrates the differences in output that arise when recognize_custom_forms
    is called with custom models trained with labeled and unlabeled data.
USAGE:
    python sample_differentiate_custom_forms_with_labeled_and_unlabeled_models_async.py

    Set the environment variables with your own values before running the sample:
    1) AZURE_FORM_RECOGNIZER_ENDPOINT - the endpoint to your Cognitive Services resource.
    2) AZURE_FORM_RECOGNIZER_KEY - your Form Recognizer subscription key
    3) CUSTOM_TRAINED_labeled_MODEL_ID - the ID of your custom model trained with labeled data
    4) CUSTOM_TRAINED_UNlabeled_MODEL_ID - the ID of your custom model trained with unlabeled data
"""

import os
import asyncio


class DifferentiateCustomFormsWithlabeledAndUnlabeledModelsAsync(object):

    endpoint = os.environ["AZURE_FORM_RECOGNIZER_ENDPOINT"]
    key = os.environ["AZURE_FORM_RECOGNIZER_KEY"]
    labeled_model_id = os.environ["CUSTOM_TRAINED_labeled_MODEL_ID"]
    unlabeled_model_id = os.environ["CUSTOM_TRAINED_UNlabeled_MODEL_ID"]

    async def recognize_custom_forms(self):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.formrecognizer.aio import FormRecognizerClient
        async with FormRecognizerClient(endpoint=self.endpoint, credential=AzureKeyCredential(self.key)) as form_recognizer_client:
            with open("sample_forms/forms/Form_1.jpg", "rb") as f:
                stream = f.read()
            forms_with_labeled_model = await form_recognizer_client.recognize_custom_forms(
                model_id=self.labeled_model_id, stream=stream
            )
            forms_with_unlabeled_model = await form_recognizer_client.recognize_custom_forms(
                model_id=self.unlabeled_model_id, stream=stream
            )

            # The main difference is found in the labels of its fields
            # The form recognized with a labeled model will have the labels it was trained with,
            # the unlabeled one will be denoted with indices
            for labeled_form in forms_with_labeled_model:
                for label, field in labeled_form.fields.items():
                    print("Field '{}' has value '{}' with a confidence score of {}".format(
                            label, field.value, field.confidence
                        ))

            for unlabeled_form in forms_with_unlabeled_model:
                for label, field in unlabeled_form.fields.items():
                    print("Field '{}' has value '{}' with a confidence score of {}".format(
                            label, field.value, field.confidence
                        ))


async def main():
    sample = DifferentiateCustomFormsWithlabeledAndUnlabeledModelsAsync()
    await sample.recognize_custom_forms()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
