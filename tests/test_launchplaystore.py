
import unittest
import pytest

from pages.playstorepage import HomeOptions


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class PlayStoreTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def launch(self, oneTimeSetUp):
      self.game = HomeOptions(self.driver)

    @pytest.mark.run(order=1)
    def test_launchapp(self):
        self.game.click_on_games()













