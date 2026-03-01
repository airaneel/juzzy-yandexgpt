import logging
from collections.abc import Generator
from typing import Optional, Union

from dify_plugin import OAICompatLargeLanguageModel
from dify_plugin.entities.model.llm import LLMResult
from dify_plugin.entities.model.message import PromptMessage, PromptMessageTool

logger = logging.getLogger(__name__)


class YandexGPTLargeLanguageModel(OAICompatLargeLanguageModel):
    def _invoke(
        self,
        model: str,
        credentials: dict,
        prompt_messages: list[PromptMessage],
        model_parameters: dict,
        tools: Optional[list[PromptMessageTool]] = None,
        stop: Optional[list[str]] = None,
        stream: bool = True,
        user: Optional[str] = None,
    ) -> Union[LLMResult, Generator]:
        self._add_custom_parameters(credentials)
        model = self._build_model_uri(model, credentials)
        return super()._invoke(
            model, credentials, prompt_messages, model_parameters,
            tools, stop, stream, user,
        )

    def validate_credentials(self, model: str, credentials: dict) -> None:
        self._add_custom_parameters(credentials)
        model = self._build_model_uri(model, credentials)
        super().validate_credentials(model, credentials)

    @staticmethod
    def _add_custom_parameters(credentials: dict) -> None:
        credentials["mode"] = "chat"
        credentials["endpoint_url"] = "https://ai.api.cloud.yandex.net/v1"

    @staticmethod
    def _build_model_uri(model: str, credentials: dict) -> str:
        """Build YandexGPT model URI: gpt://<folder_id>/<model_name>"""
        if model.startswith("gpt://"):
            return model
        folder_id = credentials.get("folder_id", "")
        return f"gpt://{folder_id}/{model}"
