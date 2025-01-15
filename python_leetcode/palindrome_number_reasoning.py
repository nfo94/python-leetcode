class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 1. Cast int para string, para facilitar a comparação
        x = str(x)
        # Obs.: lists, tuples, strings e ranges são estruturas sequenciais no Python
        # e permitem slicing

        # 2. Se x (string) for igual a x[::-1] (slice invertindo a string)
        if x == x[::-1]:
            # 3. Retorne True
            return True
        # 4. Se não é palíndrome, só podemos retornar False
        return False
