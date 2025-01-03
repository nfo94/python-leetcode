from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        # 1. Loop no array
        for index in range(len(nums)):
            # 2. Achar o número subtraindo
            complement = target - nums[index]
            # 3. O número já existe?
            if complement in num_dict:
                # 4. Retornar índex do número e do atual do loop
                return [num_dict[complement], index]
            # 5. Guardar número e índice
            num_dict[nums[index]] = index

        # 6. Retornar None se não encontrar um par
        return None
