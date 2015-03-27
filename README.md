# Pepper-Autocompmlete

A Sublime Text 3 plugin for interacting with the pepper-autocomplete service.


### Disclaimer:

This plugin is in **development** state, which means is **unstable**, and it might not work in your system. It **should** work with *Google Chrome* and *Chromium Browser* versions 31 to 34, and modern versions of *Firefox*, on modern versions of Linux, MacOSX and Windows, *but* it has only been tested so far with:

* Ubuntu Linux 13.10 x86 + ST3 (3059) + Chrome 31
* Windows 8 x64 + ST3 (3047) + Chrome 32

Current iterations are constantly changing the names, key bindings, and semantics of most commands, so every time you upgrade, something will likely not work the way it used to. Sorry for the inconvenience, I'm working as hard as possible to get a stable version out, but it will take me some time...


## What is this?

This plugin fires up a browser (Chrome and Firefox only, for now), and keeps a connection open with it, that allows you to send commands and control to the browser from within ST3.


## Installation

The recommended method is using [Sublime Package Control](https://sublime.wbond.net). If you don't know it, go check it out.

You can also [clone directly](https://github.com/apiad/sublime-browser-integration.git) from Github, or download a [zip](https://github.com/apiad/sublime-browser-integration/archive/master.zip), and unpack it in your Sublime Text 3 packages folder. If you don't know how to do this, you definitely need the Package Control plugin.

Besides that, you need a recent version of Chrome (31 to 34) and the `Chrome WebDriver` executable. Upon installation of the plugin, it will attempt to download the right executable for your platform (its about 5~10 MBs) directly from [sublime.apiad.net](http://sublime.apiad.net/browser-integration/chromedriver/) and place it in the same folder as the plugin (this only has to be done once). If this doesn't work, you can try to download it manually, rename it to `chromedriver`, place it alongside the *.sublime-package file (it should be in the root of either your `Packages/` folder or your `Installed Packages/` folder), and give it execution permissions. If this happens to you, please consider filling up the corresponding [issue](https://github.com/apiad/sublime-browser-integration/issues) to help me improve the plugin.


## Configuration

Hit `ctrl+0` to start up the browser service.
Hit `ctrl+1` for autocomplete-tabe like completions.

## Collaborating

[Github](https://github.com/tnokworks/pepper_autocomplete).

There are many ways to collaborate: just by trying it out and filling up any issues, it will be of great help.
You can also suggest changes, features, and any interesting idea.
