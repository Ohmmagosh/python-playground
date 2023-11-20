from Score import Score

class PlayerScore(Score):
	def __init__(self, player_name):
		self.super(player_name)
		self.set_table_header()


	def set_table_header(self) -> None:
		header = [
			{"title": "Date", "justify": "center", "style":"cyan"},
			{"title": "No.", "justify": "center", "style":"yellow"},
			{"title": "Quiz", "justify": "center", "style": "bright_cyan"},
			{"title": "Ans", "justify": "center", "style": "bright_white"},
		]
		return super().set_table_header(header)


	def set_row_data(self, *args):
		return super().set_row_data(*args)
