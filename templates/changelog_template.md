# CHANGELOG

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/).

{% for version in versions %}
## [{{ version.version }}]({{ version.url }}) ({{ version.date }})

{% for type in ["build", "chore", "ci", "docs", "feat", "fix", "perf", "style", "refactor", "test", "revert"] %}
{% if version.elements | selectattr("type", "equalto", type) | list | length > 0 %}
### {{ type | capitalize }}

{% for commit in version.elements if commit.type == type %}
* {{ commit.description }} ([`{{ commit.short_hash }}`]({{ commit.commit_url }}))
{% endfor %}
{% endif %}
{% endfor %}

{% endfor %}
