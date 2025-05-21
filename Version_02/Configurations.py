# bits & bytes
# Fecha: Mayo de 2025
# Descripción: version 02 Juego del gato
# Configuraciones del juego

class Configurations:
    """
    Clase que contiene todas las configuraciones del juego
    """
    #Configuraciones de la pantalla
    _screen_size = (1280, 720)            # Alto por ancho
    _game_title = "Soldiers vs aliens"  #Título del juego
    _background_image_path ="../Media/background.jpg"        #Fondo de la pantalla en
    _soldiers_image_path="../Media/soldiers.png"
    _soldiers_block_size=40
    _fps=8
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
    def get_background_image_path(cls) -> str:
        """
        Getter para _background
        return:
        """
        return cls._background_image_path

    @classmethod
    def get_soldiers_image_path(cls) -> str:
        """
        Getter para _background
        return:
        """
        return cls._soldiers_image_path

    @classmethod
    def get_soldiers_block_size(cls) ->int:
        """
        Getter para _background
        return:
        """
        return cls._soldiers_block_size

    @classmethod
    def get_fps(cls) -> int:
        """
        Getter para _background
        return:
        """
        return cls._fps