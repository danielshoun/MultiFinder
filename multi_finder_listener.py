import sublime
import sublime_plugin


class MultiFinderCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		if self.view.name() == 'Find Results':
			search_info_line = self.view.substr(self.view.line(2))
			start_of_search_term = search_info_line.index('"') + 1
			search_term = search_info_line[start_of_search_term: -1]
			self.view.set_name(f'Find Results: "{search_term}"')

class MultiFinderListener(sublime_plugin.EventListener):
	def on_new_async(self, view):
		view.run_command('multi_finder')
