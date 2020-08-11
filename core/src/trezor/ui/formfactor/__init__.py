"""
TODO docs
"""

from .. import WIDTH

if False:
    from typing import TYPE_CHECKING
    from .types import ButtonContent, ButtonStyleStateType, ButtonStyleType
else:
    TYPE_CHECKING = False

__all__ = [
    # button
    "ButtonStyleStateType",
    "ButtonStyleType",
    "ButtonContent",
    "ButtonAbort",
    "ButtonCancel",
    "ButtonClear",
    "ButtonConfirm",
    "ButtonDefault",
    "ButtonMono",
    "ButtonMonoConfirm",
    "ButtonMonoDark",
    "render_button",
    # confirm
    "DEFAULT_CANCEL",
    "DEFAULT_CANCEL_STYLE",
    "DEFAULT_CONFIRM",
    "DEFAULT_CONFIRM_STYLE",
    "confirm_button_area",
    # text
    "TEXT_HEADER_HEIGHT",
    "TEXT_LINE_HEIGHT",
    "TEXT_LINE_HEIGHT_HALF",
    "TEXT_MARGIN_LEFT",
    "TEXT_MAX_LINES",
    "header",
]

_IS_T1 = WIDTH == 128

if _IS_T1:
    from .t1.button import (
        ButtonAbort,
        ButtonCancel,
        ButtonClear,
        ButtonConfirm,
        ButtonDefault,
        ButtonMono,
        ButtonMonoConfirm,
        ButtonMonoDark,
        render_button,
    )
    from .t1.confirm import (
        DEFAULT_CANCEL,
        DEFAULT_CANCEL_STYLE,
        DEFAULT_CONFIRM,
        DEFAULT_CONFIRM_STYLE,
        confirm_button_area,
    )
    from .t1.text import (
        TEXT_HEADER_HEIGHT,
        TEXT_LINE_HEIGHT,
        TEXT_LINE_HEIGHT_HALF,
        TEXT_MARGIN_LEFT,
        TEXT_MAX_LINES,
        header,
    )

# FIXME: without the condition mypy complains about Incompatible import
elif not TYPE_CHECKING:
    from .tt.button import (
        ButtonAbort,
        ButtonCancel,
        ButtonClear,
        ButtonConfirm,
        ButtonDefault,
        ButtonMono,
        ButtonMonoConfirm,
        ButtonMonoDark,
        render_button,
    )
    from .tt.confirm import (
        DEFAULT_CANCEL,
        DEFAULT_CANCEL_STYLE,
        DEFAULT_CONFIRM,
        DEFAULT_CONFIRM_STYLE,
        confirm_button_area,
    )
    from .tt.text import (
        TEXT_HEADER_HEIGHT,
        TEXT_LINE_HEIGHT,
        TEXT_LINE_HEIGHT_HALF,
        TEXT_MARGIN_LEFT,
        TEXT_MAX_LINES,
        header,
    )
