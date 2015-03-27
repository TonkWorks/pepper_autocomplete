import re

from .pepper import *


class PepperAutoReload(sublime_plugin.EventListener):
    # def on_activated(self, view):
    #         sublime.status_message("ACTIVATED!~")

    def on_modified(self, view):
        if not browser.connected():
            return

        #not working
        if browser.pepper_ignore_changes == True:
            return
        #If its asking for key.. wait for that..
        if browser.execute("return pepper.key_entered") != "":
            settings = sublime.load_settings(SETTINGS_FILE)
            key = browser.execute("return pepper.key_entered")
            settings.set("pepper_license_key", key)

        (row,col) = view.rowcol(view.sel()[0].begin())
        char_num_for_cursor = view.sel()[0].begin()
        char_num_for_cursor_row_begin = view.sel()[0].begin() - col

        r = sublime.Region(char_num_for_cursor_row_begin, char_num_for_cursor)

        if browser.pepper_last_completion == view.substr(r):
            return

        browser.pepper_tabs = 0
        browser.last_completion = ""
        browser.pepper_last_completion_orig = ""

        #sublime.status_message("MODIFIED!~ WITH " + view.substr(r))

        settings = sublime.load_settings("Main.sublime-settings")
        key = "AAA"#settings.get('pepper_license_key')# get_setting('pepper_license_key')#get_setting("pepper_license_key", "default")
        print(key)
        browser.execute("pepper.context_change('" + view.substr(r) + "', '0', '" + key + "');")
