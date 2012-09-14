import sublime, sublime_plugin
import re

global_settings = sublime.load_settings('Switch Global.sublime-settings')


class SwitchCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        settings = self.view.settings()

        switch_definitions = settings.get('switch_custom_definitions',  [])
        switch_definitions += settings.get('switch_builtin_definitions', [])
        switch_definitions += global_settings.get('switch_custom_definitions',  [])
        switch_definitions += global_settings.get('switch_builtin_definitions', [])

        for region in self.view.sel():
            for group in switch_definitions:
                if self.apply_switch_on_region(edit, group, region):
                    break

    def apply_switch_on_region(self, edit, group, region):
        if isinstance(group, list):
            word_region = self.view.word(region)
            if self.apply_list_on_region(edit, group, word_region):
                return True
        elif isinstance(group, dict):
            line_region = self.view.line(region)
            if self.apply_dict_on_region(edit, group, line_region):
                return True
        else:
            return False

    def apply_list_on_region(self, edit, group, region):
        word_content = self.view.substr(region)

        for item_index, item in enumerate(group):
            if item == word_content:
                next_item_index = 0 if item_index >= len(group) - 1 else item_index + 1
                self.view.replace(edit, region, group[next_item_index])
                return True
        else:
            return False

    def apply_dict_on_region(self, edit, group, region):
        line_content = self.view.substr(region)

        for key, value in group.iteritems():
            match = re.search(key, line_content)
            if match:
                self.view.replace(edit, region, re.sub(key, value, line_content))
                return True
        else:
            return False
