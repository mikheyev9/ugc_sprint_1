import json

from datetime import datetime
from uuid import UUID

from models.mixins import UUIDMixin


class MessageDTO(UUIDMixin):
    user_id: UUID | str
    movie_id: str | UUID | None = None
    action: str
    event_data: str
    event_time: datetime

    @classmethod
    def from_kafka_message(cls, message: dict) -> 'MessageDTO':
        """
        Создает объект MessageDTO из сообщения Kafka.
        """
        try:
            deсode_value: dict = json.loads(message['value'].decode('utf-8'))

            user_id = deсode_value.get('user_id')
            movie_id = deсode_value.get('movie_id')
            action = message.get('key', b'').decode('utf-8')
            event_data = message.get('value', b'').decode('utf-8')

            user_id = UUID(user_id) if isinstance(user_id, str) else user_id
            movie_id = UUID(movie_id) if isinstance(movie_id, str) else movie_id

            return cls(
                user_id=user_id,
                movie_id=movie_id,
                action=action,
                event_data=event_data,
            )
        except (json.JSONDecodeError, ValueError, KeyError) as e:
            raise ValueError(f"Ошибка создание MessageDTO: {e}")
