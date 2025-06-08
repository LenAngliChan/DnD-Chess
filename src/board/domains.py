from arcade import color

from src.models.domain import Domain
from src.utils.descriptions import RED_DOMAIN_DESC, BLUE_DOMAIN_DESC, GRAY_DOMAIN_DESC
from src.utils.textures import RED_DOMAIN_TEXTURE, BLUE_DOMAIN_TEXTURE, GRAY_DOMAIN_TEXTURE


class RedDomain(Domain):
    """Красный домен"""

    def __init__(
        self,
        title: str,
    ):
        """Инициализация домена

        Args:
            title: имя домена для вывода на gui
        """
        super().__init__(
            name="Red",
            title=title,
            description=RED_DOMAIN_DESC,
            texture=RED_DOMAIN_TEXTURE,
            domain_color=color.RED,
        )


class BlueDomain(Domain):
    """Синий домен"""

    def __init__(
            self,
            title: str,
    ):
        """Инициализация домена

        Args:
            title: имя домена для вывода на gui
        """
        super().__init__(
            name="Blue",
            title=title,
            description=BLUE_DOMAIN_DESC,
            texture=BLUE_DOMAIN_TEXTURE,
            domain_color=color.BLUE,
        )


class GrayDomain(Domain):
    """Серый домен"""

    def __init__(
            self,
            title: str,
    ):
        """Инициализация домена

        Args:
            title: имя домена для вывода на gui
        """
        super().__init__(
            name="Gray",
            title=title,
            description=GRAY_DOMAIN_DESC,
            texture=GRAY_DOMAIN_TEXTURE,
            power=0,
            turn=True,
        )
