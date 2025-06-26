import pygame
from Configurations import Configurations


class Score:
    """
    Clase que maneja el marcador de aliens eliminados.

    Atributos:
        _score (int): Contador de eliminaciones
        _font (pygame.font.Font): Fuente para renderizado
        _text_color (tuple): Color RGB del texto
        _position (tuple): Posición (x,y) en pantalla
    """

    def __init__(self):
        """Inicializa el marcador con valores predeterminados"""
        self._score = 0
        self._font = pygame.font.SysFont(None, Configurations.get_score_font_size())
        self._text_color = Configurations.get_score_text_color()
        self._position = Configurations.get_score_position()

    def increase(self) -> None:
        """Incrementa el contador en 1 unidad"""
        self._score += 1

    def reset(self) -> None:
        """Reinicia el contador a 0"""
        self._score = 0

    def draw(self, screen: pygame.Surface) -> None:
        """Renderiza el marcador en la pantalla"""
        score_text = f"Aliens eliminados: {self._score}"
        text_surface = self._font.render(score_text, True, self._text_color)
        screen.blit(text_surface, self._position)

    # Getters y setters
    @property
    def score(self) -> int:
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        self._score = value