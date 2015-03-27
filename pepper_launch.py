from .pepper import *


class PepperLaunchCommand(sublime_plugin.ApplicationCommand):
    plugin_name = "Launch Browser"
    plugin_description = "Launches a new browser instance."

    @staticmethod
    def visible():
        return not browser.connected()

    @async
    def run(self):
        browsers = ['Chrome', 'Firefox22']

        @async
        def open_browser(i):
            if i < 0:
                return

            b = browsers[i]

            if browser.connected():
                with loading("Shutting down current WebDriver instance."):
                    browser.quit()

            with loading("Opening new %s instance." % b):
                browser.connect(b)
                browser.maximize_window()
                # if setting('maximize_on_startup', self):
                #     browser.maximize_window()
                # else:
                #     x, y = setting('window_position', self)
                #     w, h = setting('window_size', self)
                #     browser.set_window_position(x, y)
                #     browser.set_window_size(w, h)

            home = setting('startup_location', self)

            with loading("Loading %s" % home):
                browser.get("https://pepper-autocomplete.com/results/")

            status("%s is up and running!" % b)

        open_browser(0)
        #sublime.active_window().show_quick_panel(browsers, open_browser)
