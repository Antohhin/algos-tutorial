

# Способ через сортировку, дольше по времени но проще
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        # в этом подходе круто знать что defaultdict создаст значение по умолчанию list
        # ключи у словаря неизменяемые поэтоу надо указывать явно кортеж как неизменяемый тип данных
        ans = defaultdict(list)
        for s in strs:
            sorted_s = tuple(sorted(s))
            ans[sorted_s].append(s)
        
        return list(ans.values())
   
# решение через вектора по словам, подсчёт значений по соответствию англ алфавита в АСКИ таблице
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        # проходка по словам
        for word in strs:
            # инит вектора из нулей по кол-ву букв англ алфавита
            vector = [0] * 26
            # проход по буквам в слове для создании вектора (мапинг)
            for char in word:
                vector[ord(char) - ord('a')]+= 1
            # defaultdict на случай если нужного ключа (вектора) не найдётся
            # тк ключи неизменяемый тип данных в словаре, то использую tuple()
            mp[tuple(vector)].append(word)

        return mp.values()