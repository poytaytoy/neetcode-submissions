class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        max_frequency_count = 0
        left = 0
        longest_length = 0

        for right in range(len(s)):
            frequency[s[right]] = frequency.get(s[right], 0) + 1

            max_frequency_count = max(
                max_frequency_count,
                frequency[s[right]]
            )

            length = right - left + 1

            while length - max_frequency_count > k:
                frequency[s[left]] -= 1
                left += 1

                length = right - left + 1

            longest_length = max(longest_length, length)

        return longest_length