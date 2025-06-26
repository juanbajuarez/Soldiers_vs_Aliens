import pygame
from Configurations import Configurations


class AudioManager:
    """
    Clase que centraliza la gestión de todos los sonidos del juego.

    Atributos:
        _sounds (dict): Diccionario de efectos de sonido cargados
        _music_playing (bool): Estado de la música de fondo
    """

    def __init__(self):
        """Inicializa el sistema de audio y carga los sonidos"""
        pygame.mixer.init()
        self._sounds = {
            'shot': self._load_sound(Configurations.get_sound_shot_path()),
            'alien_hit': self._load_sound(Configurations.get_sound_alien_hit_path()),
            'game_over': self._load_sound(Configurations.get_sound_game_over_path())
        }
        self._music_playing = False

    def _load_sound(self, path: str) -> pygame.mixer.Sound:
        """Carga un efecto de sonido con la configuración de volumen"""
        sound = pygame.mixer.Sound(path)
        sound.set_volume(Configurations.get_sound_volume())
        return sound

    def play_sound(self, sound_name: str) -> None:
        """Reproduce un efecto de sonido por su clave"""
        if sound_name in self._sounds:
            self._sounds[sound_name].play()

    def play_music(self) -> None:
        """Inicia la música de fondo en loop"""
        if not self._music_playing:
            pygame.mixer.music.load(Configurations.get_music_background_path())
            pygame.mixer.music.set_volume(Configurations.get_music_volume())
            pygame.mixer.music.play(-1)  # -1 para loop infinito
            self._music_playing = True

    def stop_music(self) -> None:
        """Detiene la música de fondo"""
        pygame.mixer.music.stop()
        self._music_playing = False

    @property
    def sounds_loaded(self) -> bool:
        """Indica si los sonidos fueron cargados correctamente"""
        return len(self._sounds) > 0