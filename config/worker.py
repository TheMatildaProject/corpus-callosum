REDIS_URL = 'redis://queue:6379'

# You can also specify the Redis DB to use
# REDIS_HOST = 'redis.example.com'
# REDIS_PORT = 6380
# REDIS_DB = 3
# REDIS_PASSWORD = 'very secret'

# Queues to listen on
QUEUES = ['corpus-callosum']

# If you're using Sentry to collect your runtime exceptions, you can use this
# to configure RQ for it in a single step
SENTRY_DSN = ''