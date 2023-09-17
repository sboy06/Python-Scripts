import pyfiglet
import sys
from random import choice

figlet = pyfiglet.Figlet()

if len(sys.argv) > 1:
    flag = sys.argv[1]
    if flag in ["-f", "--font"]:
        try:
            fonts = pyfiglet.FigletFont.getFonts()
            selected_font = sys.argv[2]
            if selected_font in fonts:
                figlet = pyfiglet.Figlet(font=selected_font)
            else:
                sys.exit("Invalid font.")
        except IndexError:
            sys.exit(
                "Need to input font type. Visit for list: http://www.figlet.org/examples.html"
            )
    else:
        sys.exit("Invalid flag.")
elif len(sys.argv[1:]) == 0:
    fonts = pyfiglet.FigletFont.getFonts()
    selected_font = choice(fonts)
    figlet = pyfiglet.Figlet(font=selected_font)

text = input("Input: ")
generate = figlet.renderText(text)

print(
    f"""Output:
{generate}"""
)
