# {{ cookiecutter.project_name }}

{{ cookiecutter.project_verbose_name }}

## How This Project Was Scaffolded

This project was scaffolded using [`webyneter/wemake-django-template`](https://github.com/webyneter/wemake-django-template). Current template version is: [{% gitcommit short=True %}](https://github.com/webyneter/wemake-django-template/tree/{% gitcommit %}). See what is [updated](https://github.com/webyneter/wemake-django-template/compare/{% gitcommit %}...master) since then.

{%- if cookiecutter.meta_include %}
### Steps

```shell
# Configure the future `{{ cookiecutter.project_name }}` project:
cat << EOF > ./interior-concept-cookiecutter-config.yaml
default_context:
    project_name: "{{ cookiecutter.project_name }}"
    organization: "{{ cookiecutter.project_name }}"
    meta_include: true
    meta_output_dir: "{{ cookiecutter.meta_output_dir }}"
    async: true
    line_length: 120
    coverage_fail_under: 90
EOF

# Create the project:
cookiecutter \
  --verbose \
  --no-input \
  --overwrite-if-exists \
  --config-file ./interior-concept-cookiecutter-config.yaml \
  --output-dir {{ cookiecutter.meta_output_dir }} \
  ./wemake-django-template
```
{%- endif %}

## Prerequisites

You will need:

- `python3.11` (see `pyproject.toml` for full version)
- `postgresql` with version `15`
- Latest `docker`


## Development

When developing locally, we use:

- [`editorconfig`](http://editorconfig.org/) plugin (**required**)
- [`poetry`](https://github.com/python-poetry/poetry) (**required**)
- [`pyenv`](https://github.com/pyenv/pyenv)


## Documentation

Full documentation is available here: [`docs/`](docs).
