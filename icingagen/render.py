"""Render Icinga2 config."""
import jinja2

from .config import CONFIG_PATH


def render(*, devices, vms):
    """Render a new Icinga configuration from jinja2 template and netbox objects."""
    jinjaEnv = jinja2.Environment(loader=jinja2.FileSystemLoader(searchpath="./"))
    template = jinjaEnv.get_template(CONFIG_PATH)

    return template.render(devices=devices, vms=vms)
