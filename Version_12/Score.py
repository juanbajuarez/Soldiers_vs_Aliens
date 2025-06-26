import pygame
from Configurations import Configurations

class Score:
    """
    Clase que gestiona el marcador de aliens eliminados.
    Encargada de contar, actualizar y mostrar los puntos en pantalla.
    """

    # ─────────────────────────────────────────────
    # 1. Constructor: inicialización del marcador
    # ─────────────────────────────────────────────
    def __init__(self):
        """
        Inicializa el marcador con puntaje 0 y configura la fuente, color y posición.
        """
        self._score = 0
        self._font = pygame.font.SysFont(None, Configurations.get_score_font_size())
        self._text_color = Configurations.get_score_text_color()
        self._position = Configurations.get_score_position()

    # ─────────────────────────────────────────────
    # 2. Métodos de control de puntaje
    # ─────────────────────────────────────────────
    def increase(self) -> None:
        """Incrementa el contador de puntaje en 1."""
        self._score += 1

    def reset(self) -> None:
        """Reinicia el contador de puntaje a 0."""
        self._score = 0

    # ─────────────────────────────────────────────
    # 3. Métod0 de renderizado del marcador
    # ─────────────────────────────────────────────
    def draw(self, screen: pygame.Surface) -> None:
        """
        Dibuja el texto del marcador en pantalla.
        :param screen: Superficie donde se renderiza el marcador.
        """
        score_text = f"Aliens eliminados: {self._score}"
        text_surface = self._font.render(score_text, True, self._text_color)
        screen.blit(text_surface, self._position)

    # ─────────────────────────────────────────────
    # 4. Getters y Setters
    # ─────────────────────────────────────────────
    @property
    def score(self) -> int:
        """Devuelve el valor actual del puntaje."""
        return self._score

    @score.setter
    def score(self, value: int) -> None:
        """Establece un nuevo valor para el puntaje."""
        self._score = value
