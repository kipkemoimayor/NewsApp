import os
class Config:
    NEWS_API_URL="https://newsapi.org/v2/top-headlines?country=us&apiKey={}"
    NEWS_API_KEY=os.environ.get("NEWS_API_KEY")
    SECRET_KEY=os.environ.get("SECRET_KEY")

class ProdConfig(Config):
    pass
class DevConfig(Config):
    debug=True
config_options={
"development":DevConfig,
"production":ProdConfig
}
