"""Chrome."""

from typing import List

import selenium.webdriver
from selenium.webdriver.chrome.options import Options
from surferr.browser.browser import Browser

ARGUMENT_HEADLESS = '--headless'


class Chrome(Browser):
    """Chrome."""

    def __init__(self,
                 headless: bool = False,
                 binary_path: str = None,
                 arguments: List[str] = None) -> None:
        """Initialize object.

        Args:
            headless (bool, optional): Headless or not.
                Default to False.
            binary_path (str, optional): Binary path.
            arguments (List[str], optional): Arguments.
        """
        self.headless = headless
        super().__init__(binary_path=binary_path, arguments=arguments)
        if self.headless:
            self.arguments.append(ARGUMENT_HEADLESS)

    def launch(self) -> None:
        """Launch browser."""
        options = Options()

        if self.binary_path:
            options.binary_location = self.binary_path

        for arg in self.arguments:
            options.add_argument(arg)

        self.driver = selenium.webdriver.Chrome(options=options)

        if self.headless:
            user_agent = self.get_user_agent().replace('Headless', '')
            d = {
                'userAgent': user_agent,
                # 'platform': 'Windows',
            }
            self.driver.execute_cdp_cmd('Network.setUserAgentOverride', d)
