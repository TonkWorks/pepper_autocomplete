from .pepper import *

from .pepper_launch import *
from .pepper_quit import *
from .pepper_autocomplete import *

class PepperMainMenuCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        main_menu_commands = [
            PepperLaunchCommand,
            PepperAutocomplete,
            PepperQuitCommand
        ]

        def filter_visible(cmd):
            if not isinstance(cmd, tuple):
                if cmd.visible():
                    return cmd
                else:
                    return None

            name, desc, submenu = cmd
            submenu = [filter_visible(c) for c in submenu
                       if filter_visible(c)]

            if submenu:
                return name, desc, submenu

            return None

        main_menu_commands = [filter_visible(c) for c in main_menu_commands
                              if filter_visible(c)]

        def select_command_func(commands):
            def select_command(i):
                if i < 0:
                    return

                command = commands[i]

                if isinstance(command, tuple):
                    name, desc, l = command

                    @async
                    def quick_panel():
                        sublime.active_window().show_quick_panel([
                            [command_name(item)] +
                            command_description(item).split("\n")
                            for item in l
                        ], select_command_func(l))

                    quick_panel()

                else:
                    cmd = command_str(command)

                    if issubclass(command, sublime_plugin.ApplicationCommand):
                        sublime.run_command(cmd)
                    elif issubclass(command, sublime_plugin.WindowCommand):
                        sublime.active_window().run_command(cmd)
                    elif issubclass(command, sublime_plugin.TextCommand):
                        sublime.active_window().active_view().run_command(cmd)

            return select_command

        def command_str(cls):
            name = cls.__name__
            return "pepper_" + name[18:-7].lower()

        def command_name(cls):
            if isinstance(cls, tuple):
                name, desc, l = cls
                return name

            return cls.plugin_name

        def command_description(cls):
            if isinstance(cls, tuple):
                name, desc, l = cls
                return desc

            return cls.plugin_description

        sublime.active_window().show_quick_panel([
            [command_name(cls)] + command_description(cls).split("\n")
            for cls in main_menu_commands
        ], select_command_func(main_menu_commands))
