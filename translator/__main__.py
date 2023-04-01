import click
from .context import ContextTranslator
from .CambridgeDictionary.cambridge_translator_factory import CambridgeTranslatorFactory
from .engine import ConcreteEngineFactory
from .errors import AppError

def save_html(html):
    with open('html.html', 'w+') as f:
        f.write(html)

def read_html():
    with open('html.html', 'r') as f:
        return f.read()


def version_display():
    click.echo('Version - DEV')

def translate(word, way, engine):
    
    engine_factory = ConcreteEngineFactory()
    translator_factory = engine_factory.get_engine_factory(engine)
    translator = translator_factory.create_translator(way, word)

    ctx = ContextTranslator(translator)

    # TODO add some dicent display options
    try:
        result = ctx.translate(word)
    except AppError as e:
        click.echo('ERROR %s' % e)
        exit()

    click.echo(result)

ENGINES = ["cambridge"]

TRANSLATIONS = [
    "DEF",
    "ENG-POL",
    "ENG-GER",
]


@click.command()
@click.option('--version', '-v',is_flag=True, help='Display version of application')
@click.argument('word', type=click.STRING)
@click.argument('way', type=click.Choice(TRANSLATIONS), default="DEF")
@click.argument('engine', type=click.Choice(ENGINES), default="cambridge")
def main(version, word, way, engine):
    if version:
        version_display()
        exit()
    translate(word, way, engine)



if __name__ == '__main__':
    main()


#TODO add supoort for typos at least for cambridge dictinary
