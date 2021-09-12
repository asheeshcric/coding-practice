"""
Given a string IP, return "IPv4" if IP is a valid IPv4 address, "IPv6" if IP is a valid IPv6 address or "Neither" if IP is not a correct IP of any type.

A valid IPv4 address is an IP in the form "x1.x2.x3.x4" where 0 <= xi <= 255 and xi cannot contain leading zeros. For example, "192.168.1.1" and "192.168.1.0" are valid IPv4 addresses but "192.168.01.1", while "192.168.1.00" and "192.168@1.1" are invalid IPv4 addresses.

A valid IPv6 address is an IP in the form "x1:x2:x3:x4:x5:x6:x7:x8" where:

1 <= xi.length <= 4
xi is a hexadecimal string which may contain digits, lower-case English letter ('a' to 'f') and upper-case English letters ('A' to 'F').
Leading zeros are allowed in xi.
For example, "2001:0db8:85a3:0000:0000:8a2e:0370:7334" and "2001:db8:85a3:0:0:8A2E:0370:7334" are valid IPv6 addresses, while "2001:0db8:85a3::8A2E:037j:7334" and "02001:0db8:85a3:0000:0000:8a2e:0370:7334" are invalid IPv6 addresses.
"""
"""
Input: IP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"
Explanation: This is a valid IPv6 address, return "IPv6".
"""
from typing import List

import re


class Solution:
    def validIPAddress(self, IP: str) -> str:
        # First identify if you want to check for IPv4 or IPv6
        ip4_array = IP.split(".")
        ip6_array = IP.split(":")

        # Check for IPv4 if it matches the pattern
        if len(ip4_array) == 4 and self.check_for_IPv4(ip4_array):
            return "IPv4"

        # Check for IPv6 if it matches the pattern
        if len(ip6_array) == 8 and self.check_for_IPv6(ip6_array):
            return "IPv6"

        return "Neither"

    def has_leading_zeroes(self, num: str) -> bool:
        if len(num) == 0:
            # Empty string
            return True

        if num[0] != "0":
            return False
        else:
            return False if len(num) == 1 else True

    def is_valid_hexa(self, num):
        valid = re.sub(r"[^0-9a-fA-F]", "", num)
        return True if len(valid) == len(num) else False

    def is_valid_int(self, num):
        valid = re.sub(r"[^0-9]", "", num)
        return True if len(valid) == len(num) else False

    def check_for_IPv4(self, ip_array: List[str]) -> bool:
        # Check if there are any leading zeroes in any of the items in the array
        for num in ip_array:
            if self.has_leading_zeroes(num):
                return False

            if not self.is_valid_int(num):
                return False

            # Check if the numbers are within the range (0-255)
            if not (0 <= int(num) <= 255):
                return False

        return True

    def check_for_IPv6(self, ip_array: List[str]) -> bool:
        for num in ip_array:
            if not 0 < len(num) <= 4:
                return False

            # Check if has valid hexadecimal chars
            if not self.is_valid_hexa(num):
                return False

        return True
