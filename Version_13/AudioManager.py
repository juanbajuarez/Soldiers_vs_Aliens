import pygame
from Configurations import Configurations


class AudioManager:
    """
    Clase que centraliza la gestión de todos los sonidos del juego.

    Gestiona:
    - Efectos de sonido (disparo, impacto, game over)
    - Música de fondo

    Atributos:
        _sounds (dict): Diccionario con efectos de sonido cargados.
        _music_playing (bool): Indica si la música de fondo está sonando.
    """

    # ─────────────────────────────────────────────────────────────
    # 1. Constructor: inicializa el sistema de audio y carga sonidos
    # ─────────────────────────────────────────────────────────────
    def __init__(self):
        """Inicializa el sistema de audio y carga los efectos"""
        pygame.mixer.init()
        self._sounds = {
            'shot': self._load_sound(Configurations.get_sound_shot_path()),
            'alien_hit': self._load_sound(Configurations.get_sound_alien_hit_path()),
            'game_over': self._load_sound(Configurations.get_sound_game_over_path())
        }
        self._music_playing = False

    # ─────────────────────────────────────────────────────────────
    # 2. Cargar un sonido desde archivo y ajustar volumen
    # ─────────────────────────────────────────────────────────────
    def _load_sound(self, path: str) -> pygame.mixer.Sound:
        """
        Carga un efecto de sonido y aplica el volumen definido en configuración.
        :param path: Ruta del archivo de sonido.
        :return: Objeto pygame.mixer.Sound
        """
        sound = pygame.mixer.Sound(path)
        sound.set_volume(Configurations.get_sound_volume())
        return sound

    # ─────────────────────────────────────────────────────────────
    # 3. Reproducir efectos de sonido individuales
    # ─────────────────────────────────────────────────────────────
    def play_sound(self, sound_name: str) -> None:
        """
        Reproduce un efecto de sonido por su clave ('shot', 'alien_hit', etc.)
        :param sound_name: Clave del efecto.
        """
        if sound_name in self._sounds:
            self._sounds[sound_name].play()

    # ─────────────────────────────────────────────────────────────
    # 4. Control de música de fondo
    # ─────────────────────────────────────────────────────────────
    def play_music(self) -> None:
        """
        Inicia la música de fondo si no está activa, en loop infinito.
        """
        if not self._music_playing:
            pygame.mixer.music.load(Configurations.get_music_background_path())
            pygame.mixer.music.set_volume(Configurations.get_music_volume())
            pygame.mixer.music.play(-1)  # Repetir indefinidamente
            self._music_playing = True

    def stop_music(self) -> None:
        """
        Detiene la música de fondo.
        """
        pygame.mixer.music.stop()
        self._music_playing = False

    # ─────────────────────────────────────────────────────────────
    # 5. Verificación de estado de carga
    # ─────────────────────────────────────────────────────────────
    @property
    def sounds_loaded(self) -> bool:
        """
        Verifica si los sonidos fueron correctamente cargados.
        :return: True si hay al menos un sonido cargado.
        """
        return len(self._sounds) > 0
