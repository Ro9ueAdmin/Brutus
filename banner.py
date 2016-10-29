from pyfiglet import Figlet


def banner():
	figlet=Figlet(font='starwars')
	text="Brutus"
	print figlet.renderText(text)

