from .pepper import *


class PepperQuitCommand(sublime_plugin.ApplicationCommand):
    plugin_name = "Close Browser"
    plugin_description = "Shuts down the currently opened browser instance."

    @staticmethod
    def visible():
        return browser.connected()

    @async
    @require_browser
    def run(self):
        with loading("Shutting down browser."):
            browser.quit()
