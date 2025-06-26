class Configurations:
    """
    Clase que contiene todas las configuraciones del juego.
    """
    # Configuraciones de la pantalla.
    _game_title = "Soldados vs aliens"
    _screen_size = (1280, 720)
    _fps = 30

    # Configuraciones del soldado.
    _soldier_size = (140, 80)
    _frames_per_row = 4
    _soldier_frame_delay = 100
    _soldier_speed = 12.5

    # Configuraciones de aliens
    _alien_speed_x = 9.5
    _alien_speed_y = 9.5
    _frames_per_column = 2
    _min_aliens = 5

    # Rutas de imágenes
    _background_image_path = "../media/background.png"
    _soldier_sheet_path = "../media/soldier-idle_shooting_sheet.png"
    _shot_sheet_path = "../media/shot-sheet.png"
    _shot_size = (32, 32)
    _shot_speed = 14.5
    _aliens_Sheets = ["../media/alien1-Sheet.png", "../media/alien2-Sheet.png", "../media/alien3-Sheet.png",
                      "../media/alien4-Sheet.png", "../media/alien5-Sheet.png"]

    # Configuración de fin de juego
    _game_over_frame_count = 10
    _game_over_frames_folder = "../media/gameover"

    # Configuraciones de sonido
    _sound_shot_path = "../media/sound_shot.wav"
    _sound_alien_hit_path = "../media/sound_alien_hit.wav"
    _music_background_path = "../media/music_background.mp3"
    _sound_volume = 0.3
    _music_volume = 0.2

    # Configuraciones del marcador
    _score_font_size = 36
    _score_text_color = (255, 255, 255)  # Blanco
    _score_position = (10, 10)

    # Getters para marcador
    @classmethod
    def get_score_font_size(cls) -> int:
        return cls._score_font_size

    @classmethod
    def get_score_text_color(cls) -> tuple:
        return cls._score_text_color

    @classmethod
    def get_score_position(cls) -> tuple:
        return cls._score_position


    @classmethod
    def get_game_over_frame_count(cls) -> int:
        """
        Getter para la cantidad de frames de la animación de fin de juego.
        """
        return cls._game_over_frame_count

    @classmethod
    def get_game_over_frames_folder(cls) -> str:
        """
        Getter para la carpeta donde están los frames de la animación de fin de juego.
        """
        return cls._game_over_frames_folder

    @classmethod
    def get_aliens_Sheets(cls) -> list:
        """
        Getter para _aliens_Sheets.
        """
        return cls._aliens_Sheets

    @classmethod
    def get_game_title(cls) -> str:
        """
        Getter para _game_title.
        """
        return cls._game_title

    @classmethod
    def get_screen_size(cls) -> tuple[int, int]:
        """
        Getter para _screen_size.
        """
        return cls._screen_size

    @classmethod
    def get_shot_size(cls) -> tuple[int, int]:
        """
        Getter para _shot_size
        """
        return cls._shot_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_min_aliens(cls) -> int:
        """
        Getter para _min_aliens
        """
        return cls._min_aliens

    @classmethod
    def get_soldier_size(cls) -> tuple[int, int]:
        """
        Getter para _soldier_size.
        """
        return cls._soldier_size


    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _soldier_frames_per_row.
        """
        return cls._frames_per_row

    @classmethod
    def get_frames_per_column(cls) -> int:
        """
        Getter para _soldier_frames_per_column.
        """
        return cls._frames_per_column


    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    @classmethod
    def get_alien_speed_x(cls) -> float:
        """
        Getter para  _alien_speed_x.
        """
        return cls._alien_speed_x

    @classmethod
    def get_alien_speed_y(cls) -> float:
        """
        Getter para  _alien_speed_y.
        """
        return cls._alien_speed_y
    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed

    @classmethod
    def get_soldier_speed_y(cls) -> float:
        """
        Getter para _soldier_speed.
        """
        return cls._soldier_speed_y

    @classmethod
    def get_shot_speed(cls) -> float:
        """
        Getter para _shot_speed.
        """
        return cls._shot_speed

    @classmethod
    def get_background_image_path(cls) -> str:
        """
        Getter para _background_image_path.
        """
        return cls._background_image_path


    @classmethod
    def get_soldier_sheet_path(cls) -> str:
        """
        Getter para _soldier_sheet_path.
        """
        return cls._soldier_sheet_path

    @classmethod
    def get_shot_sheet_path(cls) -> str:
        """
        Getter para _shot_sheet_path.
        """
        return cls._shot_sheet_path