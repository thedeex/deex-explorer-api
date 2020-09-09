import os


WEBSOCKET_URL = os.environ.get('WEBSOCKET_URL', "")


# Default connection to Elastic Search.
ELASTICSEARCH = {
     #'hosts': os.environ.get('ELASTICSEARCH_URL', 'https://elasticsearch.deex-kibana.info/').split(','),
     'hosts': os.environ.get('ELASTICSEARCH_URL', 'https://127.0.0.1').split(','),
     'user': os.environ.get('ELASTICSEARCH_USER', 'DeEx'),
     'password': os.environ.get('ELASTICSEARCH_PASS', 'Infrastructure')
}


# Optional ElasticSearch cluster to access other data.
# Currently expect:
#   - 'operations': for deex-* indexes where operations are stored
#   - 'objects': for objects-* indexes where Chain data is stored.
#
# Sample:
#
# ELASTICSEARCH_ADDITIONAL {
#   'operations': None, # Use default cluster.
#   'objects': {
#     'hosts': ['https://es.mycompany.com/'],
#     'user': 'myself',
#     'password': 'secret'
#    }
# }
ELASTICSEARCH_ADDITIONAL = {
    # Overwrite cluster to use to retrieve deex-* index.
    'operations': None,
    # Overwrite cluster to use to retrieve deex-* index.
    'objects': {
        #'hosts': ['https://elasticsearch.deex-kibana.info/'] # oxarbitrage (no credentials)
        'hosts': ['https://DeEx:Infrastructure@eu.elasticsearch.deex.ws:443'] # infra
    }

}

# Cache: see https://flask-caching.readthedocs.io/en/latest/#configuring-flask-caching
CACHE = {
    'CACHE_TYPE': os.environ.get('CACHE_TYPE', 'simple'), # use 'uwsgi' when running under uWSGI server.
    'CACHE_DEFAULT_TIMEOUT': int(os.environ.get('CACHE_DEFAULT_TIMEOUT', 600)) # 10 min
}

# Configure profiler: see https://github.com/muatik/flask-profiler
PROFILER = {
    'enabled': os.environ.get('PROFILER_ENABLED', False),
    'username': os.environ.get('PROFILER_USERNAME', None),
    'password': os.environ.get('PROFILER_PASSWORD', None),
}

CORE_ASSET_SYMBOL = 'DEEX'
CORE_ASSET_ID = '1.3.0'

TESTNET = 0 # 0 = not in the testnet, 1 = testnet
CORE_ASSET_SYMBOL_TESTNET = 'TEST'

# Choose which APIs to expose, default to all.
#EXPOSED_APIS = ['explorer', 'es_wrapper', 'udf']
