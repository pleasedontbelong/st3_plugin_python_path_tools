# -*- coding: utf-8 -*-

import os

import sublime
import sublime_plugin


class CopyPythonPathCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        python_path_items = []
        head, tail = os.path.split(self.view.file_name())

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
        caret_point = self.view.sel()[0].begin()
        if 'entity.name.class.python' in self.view.scope_name(caret_point):
            python_path_items.append(self.view.substr(self.view.word(caret_point)))

        if 'entity.name.function.python' in self.view.scope_name(caret_point):
            method_name = self.view.substr(self.view.word(caret_point))
            if self.view.indentation_level(caret_point) > 0:
                regions = self.view.find_by_selector('entity.name.class.python')
                possible_class_point = 0
                regions = list(filter(lambda reg: reg.b < caret_point, regions))

                for region in reversed(regions):
                    if self.view.indentation_level(region.a) == 0:
                        possible_class_point = region.a
                        break

                class_name = self.view.substr(self.view.word(possible_class_point))

                python_path_items.append(class_name)

            python_path_items.append(method_name)

        python_path = '.'.join(python_path_items)
        sublime.set_clipboard(python_path)

        sublime.status_message('"%s" copied to clipboard' % python_path)

    def is_enabled(self):
        matcher = 'source.python'
        return self.view.match_selector(self.view.sel()[0].begin(), matcher)
