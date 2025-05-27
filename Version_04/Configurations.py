# Juan Bautista Juárez
# Fecha: 21 de Mayo de 2025
# Descripción: version 04 Juego del gato
# Configuraciones del juego.

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)            # Alto por ancho
    _game_title = "Juego nuevo"  #Título del juego
    _background = (255, 100, 100)          #Fondo de la pantalla en RGB
    _fps = 8
    _solder_size=(250,250)
    _soldier_speed=10

    # Rutas de las imágenes utilizadas para las clases Background, SnakeBlock y Apple.
    _background_image_path = "../Media/background_image.jpg"
    _soldier_image_path= "../Media/solders_image.png"

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
    def get_soldier_image_path(cls) -> str:
        """
        Getter para _soldier_image_path.
        """
        return cls._soldier_image_path

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _fps.
        """
        return cls._fps

    @classmethod
    def get_solder_size(cls) -> tuple[int, int]:
        """
        Getter para _solder_size
        :return:
        """
        return cls._solder_size

    @classmethod
    def get_soldier_speed(cls) -> int:
        """
        Getter para _solder_size
        :return:
        """
        return cls._soldier_speed
