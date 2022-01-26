import json
import click
import sys

from traitlets.config import Config


def pdf_config_setup(config_settings):
    config = Config()

    if config_settings is None:
        pass
    elif config_settings == "no-code":
        config.TemplateExporter.exclude_output_prompt = True
        config.TemplateExporter.exclude_input = True
        config.TemplateExporter.exclude_input_prompt = True
    else:
        try:
            config_dict = json.loads(config_settings)
        except:
            click.secho(
                "Config setting supplied in incorrect format. Expected either a preset config: no-code, or a JSON object of settings as a string."
            )
            sys.exit(1)
        config = Config(config_dict)

    return config
