from pyweblog import SetupLogger

logger = SetupLogger(
    username='test@test.com',
    password='test',
)
logger.error('test')