# Copyright (c) Microsoft Corporation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from playwright import Error


async def test_ignore_https_error_should_work(browser, https_server):
    context = await browser.newContext(ignoreHTTPSErrors=True)
    page = await context.newPage()
    response = await page.goto(https_server.EMPTY_PAGE)
    assert response.ok
    await context.close()


async def test_ignore_https_error_should_work_negative_case(browser, https_server):
    context = await browser.newContext()
    page = await context.newPage()
    with pytest.raises(Error):
        await page.goto(https_server.EMPTY_PAGE)
    await context.close()