"""
Copyright 2018 Arm Ltd.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

SPDX-License-Identifier: Apache-2.0
"""

from .localization import _
from .cross_compile_issue import CrossCompileIssue


class HostCpuDetectionIssue(CrossCompileIssue):
    def __init__(self, filename, lineno, condition):
        description = _("condition checks host CPU (not cross-compile friendly): %s") % \
            condition
        super().__init__(description=description, filename=filename,
                         lineno=lineno)
