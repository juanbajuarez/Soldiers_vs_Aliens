import pygame

class Configurations:
    """
    Clase que centraliza todas las configuraciones del juego:
    pantalla, personajes, imágenes, sonidos y controles.
    """

    # ─────────────────────────────────────────────
    # 1. Configuración general de la pantalla
    # ─────────────────────────────────────────────
    _game_title = "Soldados vs aliens"
    _screen_size = (1280, 720)
    _fps = 30

    # ─────────────────────────────────────────────
    # 2. Configuración del soldado (jugadores)
    # ─────────────────────────────────────────────
    _soldier_size = (140, 80)
    _soldier2_size = (140, 80)
    _frames_per_row = 4
    _frames_per_column = 2
    _soldier_frame_delay = 100
    _soldier_speed = 12.5

    # ─────────────────────────────────────────────
    # 3. Configuración de los aliens
    # ─────────────────────────────────────────────
    _alien_speed_x = 9.5
    _alien_speed_y = 9.5
    _min_aliens = 5

    # ─────────────────────────────────────────────
    # 4. Configuración de disparos
    # ─────────────────────────────────────────────
    _shot_size = (32, 32)
    _shot_speed = 14.5

    # ─────────────────────────────────────────────
    # 5. Rutas de imágenes
    # ─────────────────────────────────────────────
    _background_image_path = "../media/background.png"
    _soldier_sheet_path = "../media/soldier-idle_shooting_sheet.png"
    _shot_sheet_path = "../media/shot-sheet.png"
    _aliens_sheets = [
        "../media/alien1-Sheet.png",
        "../media/alien2-Sheet.png",
        "../media/alien3-Sheet.png",
        "../media/alien4-Sheet.png",
        "../media/alien5-Sheet.png"
    ]
    _soldier_kill = "../media/animation_kill.png"
    _game_over_image_path = "../media/game_over.png"

    # ─────────────────────────────────────────────
    # 6. Configuración de animación de Game Over
    # ─────────────────────────────────────────────
    _game_over_size = (500, 300)
    _frames_per_row_kills = 6
    _game_over_frame_count = 10
    _game_over_frames_folder = "../media/gameover"

    # ─────────────────────────────────────────────
    # 7. Configuración de audio
    # ─────────────────────────────────────────────
    _sound_shot_path = "../media/sound_shot.mp3"
    _sound_alien_hit_path = "../media/sound_alien_hit.mp3"
    _sound_game_over_path = "../media/sound_game_over.mp3"
    _music_background_path = "../media/music_background.mp3"
    _sound_volume = 0.4
    _music_volume = 0.3

    # ─────────────────────────────────────────────
    # 8. Configuración del marcador
    # ─────────────────────────────────────────────
    _score_font_size = 36
    _score_text_color = (255, 255, 255)
    _score_position = (10, 10)

    # ─────────────────────────────────────────────
    # 9. Controles del segundo jugador
    # ─────────────────────────────────────────────
    _second_player_controls = {
        "move_up": pygame.K_w,
        "move_down": pygame.K_s,
        "shoot": pygame.K_d
    }

    # ─────────────────────────────────────────────
    # GETTERS
    # ─────────────────────────────────────────────

    # Pantalla
    @classmethod
    def get_game_title(cls) -> str:
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        return cls._screen_size

    @classmethod
    def get_fps(cls) -> int:
        return cls._fps

    # Soldado
    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        return cls._soldier_size

    @classmethod
    def get_soldier2_size(cls) -> tuple[int, int]:
        return cls._soldier2_size

    @classmethod
    def get_frames_per_row(cls) -> int:
        return cls._frames_per_row

    @classmethod
    def get_frames_per_column(cls) -> int:
        return cls._frames_per_column

    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        return cls._soldier_frame_delay

    @classmethod
    def get_soldier_speed(cls) -> float:
        return cls._soldier_speed

    # Aliens
    @classmethod
    def get_alien_speed_x(cls) -> float:
        return cls._alien_speed_x

    @classmethod
    def get_alien_speed_y(cls) -> float:
        return cls._alien_speed_y

    @classmethod
    def get_min_aliens(cls) -> int:
        return cls._min_aliens

    # Disparos
    @classmethod
    def get_shot_size(cls) -> tuple[int, int]:
        return cls._shot_size
    @classmethod
    def get_shot_speed(cls) -> float:
        return cls._shot_speed

    # Imágenes
    @classmethod
    def get_background_image_path(cls) -> str:
        return cls._background_image_path
    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        return cls._shot_sheet_path

    @classmethod
    def get_aliens_sheets(cls) -> list:
        return cls._aliens_sheets
    @classmethod
    def get_soldier_kill(cls) -> str:
        return cls._soldier_kill

    @classmethod
    def get_game_over_image_path(cls) -> str:
        return cls._game_over_image_path

    # Animación Game Over
    @classmethod
    def get_game_over_size(cls) -> tuple[int, int]:
        return cls._game_over_size

    @classmethod
    def get_frames_per_row_kills(cls) -> int:
        return cls._frames_per_row_kills

    @classmethod
    def get_game_over_frame_count(cls) -> int:
        return cls._game_over_frame_count

    @classmethod
    def get_game_over_frames_folder(cls) -> str:
        return cls._game_over_frames_folder

    # Audio
    @classmethod
    def get_sound_shot_path(cls) -> str:
        return cls._sound_shot_path

    @classmethod
    def get_sound_alien_hit_path(cls) -> str:
        return cls._sound_alien_hit_path

    @classmethod
    def get_sound_game_over_path(cls) -> str:
        return cls._sound_game_over_path

    @classmethod
    def get_music_background_path(cls) -> str:
        return cls._music_background_path

    @classmethod
    def get_sound_volume(cls) -> float:
        return cls._sound_volume

    @classmethod
    def get_music_volume(cls) -> float:
        return cls._music_volume

    # Marcador
    @classmethod
    def get_score_font_size(cls) -> int:
        return cls._score_font_size
    @classmethod
    def get_score_text_color(cls) -> tuple:
        return cls._score_text_color
    @classmethod
    def get_score_position(cls) -> tuple:
        return cls._score_position

    # Controles jugador 2
    @classmethod
    def get_second_player_controls(cls) -> dict:
        return cls._second_player_controls
