# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
# Licensed under the Apache License, Version 2.0 (the “License”);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an “AS IS” BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========== Copyright 2023 @ CAMEL-AI.org. All Rights Reserved. ===========
from dataclasses import dataclass, field
from typing import Dict, Optional, Sequence, Union


@dataclass(frozen=True)
class ChatGPTConfig:
    r"""Defines the parameters for generating chat completions using the
    OpenAI API.

    Args:
        temperature (float, optional): Sampling temperature to use, between
            :obj:`0` and :obj:`2`. Higher values make the output more random,
            while lower values make it more focused and deterministic.
            (default: :obj:`0.2`)
        top_p (float, optional): An alternative to sampling with temperature,
            called nucleus sampling, where the model considers the results of
            the tokens with top_p probability mass. So :obj:`0.1` means only
            the tokens comprising the top 10% probability mass are considered.
            (default: :obj:`1.0`)
        n (int, optional): How many chat completion choices to generate for
            each input message. ()default: :obj:`1`)
        stream (bool, optional): If True, partial message deltas will be sent
            as data-only server-sent events as they become available.
            (default: :obj:`False`)
        stop (str or list, optional): Up to :obj:`4` sequences where the API
            will stop generating further tokens. (default: :obj:`None`)
        max_tokens (int, optional): The maximum number of tokens to generate
            in the chat completion. The total length of input tokens and
            generated tokens is limited by the model's context length.
            (default: :obj:`None`)
        presence_penalty (float, optional): Number between :obj:`-2.0` and
            :obj:`2.0`. Positive values penalize new tokens based on whether
            they appear in the text so far, increasing the model's likelihood
            to talk about new topics. See more information about frequency and
            presence penalties. (default: :obj:`0.0`)
        frequency_penalty (float, optional): Number between :obj:`-2.0` and
            :obj:`2.0`. Positive values penalize new tokens based on their
            existing frequency in the text so far, decreasing the model's
            likelihood to repeat the same line verbatim. See more information
            about frequency and presence penalties. (default: :obj:`0.0`)
        logit_bias (dict, optional): Modify the likelihood of specified tokens
            appearing in the completion. Accepts a json object that maps tokens
            (specified by their token ID in the tokenizer) to an associated
            bias value from :obj:`-100` to :obj:`100`. Mathematically, the bias
            is added to the logits generated by the model prior to sampling.
            The exact effect will vary per model, but values between:obj:` -1`
            and :obj:`1` should decrease or increase likelihood of selection;
            values like :obj:`-100` or :obj:`100` should result in a ban or
            exclusive selection of the relevant token. (default: :obj:`{}`)
        user (str, optional): A unique identifier representing your end-user,
            which can help OpenAI to monitor and detect abuse.
            (default: :obj:`""`)
    """
    temperature: float = 0.2  # openai default: 1.0
    top_p: float = 1.0
    n: int = 1
    stream: bool = False
    stop: Optional[Union[str, Sequence[str]]] = None
    max_tokens: Optional[int] = None
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0
    logit_bias: Dict = field(default_factory=dict)
    user: str = ""
