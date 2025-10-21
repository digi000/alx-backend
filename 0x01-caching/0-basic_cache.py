#!/usr/bin/python3
"""class BasicCache that inherits from BaseCaching"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """basic caching system"""
    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value for the key key"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
