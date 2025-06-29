# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 05 Juego del alien
# Configuraciones del juego.

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)            # Alto por ancho
    _game_title = "Soldiers vs aliens"  #Título del juego
    _background = (255, 100, 100)          #Fondo de la pantalla en RGB
    _fps = 100
    _solder_size=(250,250)
    _shot_size=(70,70)
    _frames_per_row = 4
    _soldier_frame_delay = 300
    _shot_frame_delay = 150
    _soldier_speed = 24.5
    _shot_speed = 10

    # Rutas de las imágenes utilizadas para las clases Background, SnakeBlock y Apple.
    _background_image_path = "../Media/background_image.jpg"
    _soldier_sheet_path="../Media/soldier-idle-sheet.png"
    _shot_sheet_path="../Media/shot-sheet.png"
    #Métodos de acceso

    @classmethod
    def get_screen_size(cls)->tuple[int,int]:
        """
        Getter para _screen_size
        :return:
        """
        return cls._screen_size
    @classmethod
    def get_game_title(cls)->str:
        """
        Getter para _game_title
        :return:
        """
        return cls._game_title

    @classmethod
    def get_background(cls) -> tuple[int,int,int]:
        """
        Getter para _background
        :return:
        """
        return cls._background

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

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_frames_per_row(cls) -> int:
        """
        Getter para _frames_per_row.
        """
        return cls._frames_per_row

    @classmethod
    def get_solder_size(cls) -> tuple[int, int]:
        """
        Getter para _solder_size
        :return:
        """
        return cls._solder_size

    @classmethod
    def get_shot_size(cls) -> tuple[int, int]:
        """
        Getter para _shot_size
        :return:
        """
        return cls._shot_size
    @classmethod
    def get_soldier_speed(cls) -> float:
        """
        Getter para _solder_size
        :return:
        """
        return cls._soldier_speed

    @classmethod
    def get_shot_speed(cls) -> float:
        """
        Getter para _shot_speed
        :return:
        """
        return cls._shot_speed


    @classmethod
    def get_soldier_frame_delay(cls) -> int:
        """
        Getter para _soldier_frame_delay.
        """
        return cls._soldier_frame_delay

    @classmethod
    def get_shot_frame_delay(cls) -> int:
        """
        Getter para _shot_frame_delay.
        """
        return cls._shot_frame_delay