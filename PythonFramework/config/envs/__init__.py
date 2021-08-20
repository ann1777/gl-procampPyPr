import collections
from providers import providers
import self as self
from data.service.browsers_provider import provider

class HierarchicalProvider(ConfigKeyProvider):
    """
    In case it not configured from the one in the passed...
    """
    
    def __init__(self, None):
        self.ConfigKeyProvider = ConfigKeyProvider
        self.providers = providers

    def add(self, provider):
        """
        :param ConfigKeyProvider: Single item or list of ConfigKeyProvider
        """
            self.provider.append(provider)
        else:
            raise ValueError("Provider must be of ConfigKeyProvider")
        if isinstance(providers, collections.Sequence):
            for item in providers:
                provider.add_checked(item)
