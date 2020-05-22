# -*- coding: utf-8 -*-

import os

import sublime
import sublime_plugin


class CopyImportFirstDefinitionCommand(sublime_plugin.TextCommand):

    def get_path_items(self, location):
        print(location)
        python_path_items = []
        head, tail = os.path.split(location)

        module = tail.rsplit('.', 1)[0]
        if module != '__init__':
            python_path_items.append(module)

        head, tail = os.path.split(head)

        while tail:
            if '__init__.py' in os.listdir(os.path.join(head, tail)):
                python_path_items.insert(0, tail)
            else:
                break

            head, tail = os.path.split(head)
        return python_path_items

    def run(self, edit):
        caret_point = self.view.sel()[0].begin()
        word = self.view.substr(self.view.word(caret_point))
        location = self.view.window().lookup_symbol_in_index(word)
        if not location:
            return
        import_string = "from {} import {}".format(
            ".".join(self.get_path_items(location[0][0])),
            word
        )
        sublime.set_clipboard(import_string)
        sublime.status_message('"%s" copied to clipboard' % import_string)

    def is_enabled(self):
        matcher = 'source.python'
        return self.view.match_selector(self.view.sel()[0].begin(), matcher)
