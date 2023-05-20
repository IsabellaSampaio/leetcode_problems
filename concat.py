class Solution:
	def findAllConcatenatedWords(self, words):
		wordDict = set(words)
		cache = {}
		return [word for word in words if self._canForm(word, wordDict, cache)]

	def _canForm(self, word, wordDict, cache):
		if word in cache: 
			return cache[word]

		for index in range (1, len(word)):
			prefix = word[:index]
			suffix = word[index:]
			if prefix in wordDict:
				if suffix in wordDict or self._canForm(suffix, wordDict, cache):
					return True
		return False


input = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
print(Solution().findAllConcatenatedWords(input))


