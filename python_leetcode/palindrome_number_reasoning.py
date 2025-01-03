class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Cast int para string, para facilitar a comparação
        x = str(x)
        # 2. Se x (string) for igual a x[::-1] (slice invertindo a string)
        if x == x[::-1]:
            # 3. Retorne True
            return True
        # 4. Se não, retorne False
        return False
