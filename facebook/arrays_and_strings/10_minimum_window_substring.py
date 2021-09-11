class Solution:
    """
    1. First create two hashMaps:
        - current_window: keeps track of the letter counts in the current window
        - need_chars: Fixed count of the number of each char needed
    2. left=0 and loop through the main string as right as the index
    3. Whenever you find a char that you need, increase have += 1
    4. When need == have:
        - Run a while loop and keep popping chars from the left until have != need
    5. Now, if the current_substring s[left:right+1] is smaller than the previous result, store the lenght
    and the indices
    6. Return the slice at the end: return s[left:right+1]

    """

    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        need_chars, current_window = dict(), dict()
        for char in t:
            need_chars[char] = need_chars.get(char, 0) + 1

        have, need = 0, len(need_chars.keys())
        res_len, res_idx = len(s)+1, [0, 0]
        left = 0
        for right, char in enumerate(s):
            # Add the char to the current window
            current_window[char] = current_window.get(char, 0) + 1
            if char in need_chars and current_window[char] == need_chars[char]:
                have += 1

            while have == need:
                current_len = right - left + 1
                if current_len < res_len:
                    res_len = current_len
                    res_idx = [left, right]

                # Pop the leftmost char from the window
                current_window[s[left]] -= 1
                if s[left] in need_chars and current_window[s[left]] < need_chars[s[left]]:
                    # This means we have taken out a necessary char to make a valid substring
                    have -= 1

                # Move the left pointer by 1
                left += 1

        l, r = res_idx
        return s[l:r+1] if res_len != len(s)+1 else ""
