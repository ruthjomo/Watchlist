class Config:
    '''
    General configuration parent class
    '''
    pass
 MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{a7a73322f9c341657cbb9517ad5fe145}?api_key={a7a73322f9c341657cbb9517ad5fe145}'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True