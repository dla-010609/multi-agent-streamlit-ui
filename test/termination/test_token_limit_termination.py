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
import pytest

from camel.termination import TokenLimitTermination


@pytest.mark.parametrize('num_tokens', [5, 10])
def test_token_limit_termination(num_tokens):
    termination = TokenLimitTermination(token_limit=10)
    terminated, termination_reasons = termination.terminated(
        num_tokens=num_tokens)
    if num_tokens == 5:
        assert not terminated
        assert termination_reasons == []
    if num_tokens == 10:
        assert terminated
        assert termination_reasons[0] == "max_tokens_exceeded"
