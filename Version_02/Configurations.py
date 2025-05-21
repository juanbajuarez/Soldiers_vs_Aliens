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
    _game_title = "Juego nuevo"  #Título del juego
    _background = (255, 100, 100)          #Fondo de la pantalla en RGB

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
        return:
        """
        return cls._background