
from dynaconf import Dynaconf
import os
settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=[os.getcwd()+'/config/settings.toml', os.getcwd()+'/config/.secrets.toml'],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
