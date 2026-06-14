from handlers.main_handlers import register_main_handlers
from handlers.svo_handlers import register_svo_handlers
from handlers.large_handlers import register_large_handlers
from handlers.laws_handlers import register_laws_handlers
from handlers.common_handlers import register_common_handlers

__all__ = [
    'register_main_handlers',
    'register_svo_handlers',
    'register_large_handlers',
    'register_laws_handlers',
    'register_common_handlers'
]