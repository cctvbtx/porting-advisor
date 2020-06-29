"""
Copyright 2017-2020 Arm Ltd.

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

import sys


from .issue_type_config import IssueTypeConfig
from .report_item import ReportItem
from .scanner import Scanner

class IssueTypeFilter(Scanner):
    """Filters issues by type."""

    def __init__(self, issue_type_config):
        """Filters issues by type.

        Args:
            issue_type_config (IssueTypeConfig): issue type filter configuration
        """
        self.issue_type_config = issue_type_config

    def finalize_report(self, report):
        report.issues = [issue for issue in report.issues if self.issue_type_config.include_issue_p(issue)]
