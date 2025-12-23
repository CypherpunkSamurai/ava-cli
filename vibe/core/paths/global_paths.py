from __future__ import annotations

from collections.abc import Callable
import os
from pathlib import Path

from vibe import VIBE_ROOT


class GlobalPath:
    def __init__(self, resolver: Callable[[], Path]) -> None:
        self._resolver = resolver

    @property
    def path(self) -> Path:
        return self._resolver()


_DEFAULT_AVA_HOME = Path.home() / ".ava"


def _get_ava_home() -> Path:
    if ava_home := os.getenv("AVA_HOME"):
        return Path(ava_home).expanduser().resolve()
    return _DEFAULT_AVA_HOME


AVA_HOME = GlobalPath(_get_ava_home)
GLOBAL_CONFIG_FILE = GlobalPath(lambda: AVA_HOME.path / "config.toml")
GLOBAL_ENV_FILE = GlobalPath(lambda: AVA_HOME.path / ".env")
GLOBAL_TOOLS_DIR = GlobalPath(lambda: AVA_HOME.path / "tools")
SESSION_LOG_DIR = GlobalPath(lambda: AVA_HOME.path / "logs" / "session")
TRUSTED_FOLDERS_FILE = GlobalPath(lambda: AVA_HOME.path / "trusted_folders.toml")
LOG_DIR = GlobalPath(lambda: AVA_HOME.path / "logs")
LOG_FILE = GlobalPath(lambda: AVA_HOME.path / "ava.log")

DEFAULT_TOOL_DIR = GlobalPath(lambda: VIBE_ROOT / "core" / "tools" / "builtins")
