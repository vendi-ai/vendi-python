"""
Vendi is a Python client for the Vendi API. It provides a convenient way to access the Vendi API from a Python application.
This is the main entrypoint for the Vendi SDK.
"""
from vendi_sdk.core.config import vendi_config
from vendi_sdk.datasets import Datasets
from vendi_sdk.finetune import Finetune
from vendi_sdk.deployments.deployments import Deployments
from vendi_sdk.models import Models
from vendi_sdk.completions import Completions
from vendi_sdk.runtime import Runtime
from vendi_sdk.runtime.decorators import task, workflow
from vendi_sdk.runtime.instrument import Instrument
from vendi_sdk.runtime.feedback import Feedback
import os

VENDI_API_URL = vendi_config.VENDI_API_URL


class Vendi:

    def __init__(
            self,
            *,
            api_url: str | None = None,
            api_key: str | None = None,
            project_id: str | None = None,
    ):
        self._base_url = api_url or vendi_config.VENDI_API_URL

        if api_key:
            self.api_key = api_key
            # TODO: find a better way to set the api key for Instrument
            os.environ['VENDI_API_KEY'] = api_key
        else:
            self.api_key = vendi_config.VENDI_API_KEY

        self._project_id = project_id
        self.models = Models(url=self._base_url, api_key=self.api_key)
        self.deployments = Deployments(url=self._base_url, api_key=self.api_key)
        self.datasets = Datasets(url=self._base_url, api_key=self.api_key)
        self.completions = Completions(url=self._base_url, api_key=self.api_key)
        self.finetune = Finetune(url=self._base_url, api_key=self.api_key)
        self.runtime = Runtime(url=self._base_url, api_key=self.api_key, project_id=self._project_id)
        self.instrument = Instrument
        self.task = task
        self.workflow = workflow
        self.feedback = self.runtime.feedback
        self.afeedback = self.runtime.afeedback
