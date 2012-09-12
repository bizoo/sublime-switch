import sublime, sublime_plugin, re

settings = sublime.load_settings('Switch.sublime-settings')

class Pref:
  def load(self):
    Pref.switch_definitions = settings.get('switch_definitions')

Pref = Pref()
Pref.load()

settings.add_on_change('reload', lambda:Pref.load())

class SwitchCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for region in self.view.sel():
      for extension, switches in Pref.switch_definitions.iteritems():
        if extension == "*" or extension == self.view.file_name().split(".")[-1]:
          if self.apply_switches_on_region(edit, switches, region): break

  def apply_switches_on_region(self, edit, switches, region):
    word_region  = self.view.word(region)
    line_region  = self.view.line(region)

    for switch, group in switches.iteritems():
      if isinstance(group, list):
        if self.apply_list_on_region(edit, group, word_region): return True
      elif isinstance(group, dict):
        if self.apply_dict_on_region(edit, group, line_region): return True
    else: return False

  def apply_list_on_region(self, edit, group, region):
    word_content = self.view.substr(region)

    for item_index, item in enumerate(group):
      if item == word_content:
        next_item_index = 0 if item_index >= len(group) - 1 else item_index + 1
        self.view.replace(edit, region, group[next_item_index])
        return True
    return False

  def apply_dict_on_region(self, edit, group, region):
    line_content = self.view.substr(region)

    for key, value in group.iteritems():
      match = re.search(key, line_content)
      if match:
        self.view.replace(edit, region, re.sub(key, value, line_content))
        return True
    else: return False
