from .pepper import *

class PepperAutocomplete(sublime_plugin.TextCommand):
    plugin_name = "Autocomplete"
    plugin_description = "Autocompletes text."

    @staticmethod
    def visible():
        return browser.connected()

    @require_browser
    def run(self, edit):
        view = sublime.active_window().active_view()
        (row,col) = view.rowcol(view.sel()[0].begin())
        char_num_for_cursor = view.sel()[0].begin()
        char_num_for_cursor_row_begin = view.sel()[0].begin() - col
        r = sublime.Region(char_num_for_cursor_row_begin, char_num_for_cursor)


        browser.pepper_ignore_changes = True #Do not search using autocomplete results #DOES NOT WORk!?



        if browser.pepper_tabs > 0:
            rr = sublime.Region(char_num_for_cursor_row_begin - len(browser.pepper_last_completion), char_num_for_cursor)
            view.erase(edit, rr)


        (row,col) = view.rowcol(view.sel()[0].begin())
        char_num_for_cursor = view.sel()[0].begin()
        char_num_for_cursor_row_begin = view.sel()[0].begin() - col
        r = sublime.Region(char_num_for_cursor_row_begin, char_num_for_cursor)

        if browser.pepper_last_completion_orig == "":
            browser.pepper_last_completion_orig = view.substr(r)

        completion_string = browser.execute("return pepper.tab_complete_string('" + browser.pepper_last_completion_orig + "', " + str(browser.pepper_tabs) + ");")

        if completion_string:

            line = view.line(r)
            #edit = view.begin_edit()
            if browser.pepper_tabs > 0:
                completion_string = browser.pepper_last_completion_orig + completion_string
            view.insert(edit, col, completion_string)
        browser.pepper_tabs += 1

        browser.pepper_ignore_changes = False
        (row,col) = view.rowcol(view.sel()[0].begin())
        char_num_for_cursor = view.sel()[0].begin()
        char_num_for_cursor_row_begin = view.sel()[0].begin() - col
        r = sublime.Region(char_num_for_cursor_row_begin, char_num_for_cursor)

        browser.pepper_last_completion = view.substr(r)
