from pymongo import MongoClient

__author__ = 'Jacek Aleksander Gruca'


# This class abstracts the queue stored via the persistence abstraction
class Queue(object):
	#
	def __init__(self, store):
		self.client = MongoClient()
		self.db = self.client['twitterbot']
		self.queue = self.client.twitterbot['queue']
		self.store = store

	def get_all_handles(self):
		handles = []
		for handle in self.queue.find():
			handles.append(handle['twitter_handle'])
		return handles

	def remove_handles(self, handles_to_remove):
		for handle in handles_to_remove:
			self.queue.delete_one({'twitter_handle': handle})

	def append_handles(self, handles_to_append):
		for handle in handles_to_append:
			self.queue.insert({'twitter_handle': handle})
