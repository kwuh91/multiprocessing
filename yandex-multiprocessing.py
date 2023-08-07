from multiprocessing import Process, Manager

flag: bool = True
str1: str
str2: str


def DRY(hashmap: dict[str, [int]], string: str, length: int) -> None:
    hashmap.clear()
    for i in range(length):
        if string[i] not in hashmap:
            hashmap[string[i]] = [i]
        else:
            hashmap[string[i]].append(i)


if __name__ == '__main__':
    n = int(input())
    flag = True
    manager = Manager()
    hash1 = manager.dict()
    hash2 = manager.dict()
    for _ in range(n):
        str1 = input()
        str2 = input()
        size = len(str1)
        procs = []

        proc = Process(target=DRY, args=(hash1, str1, size))
        procs.append(proc)
        proc.start()

        proc = Process(target=DRY, args=(hash2, str2, size))
        procs.append(proc)
        proc.start()

        for proc in procs:
            proc.join()

        for j in range(size):
            if hash1[str1[j]] != hash2[str2[j]]:
                print(f"NO")
                flag = False
                break

        if flag:
            print(f"YES")
