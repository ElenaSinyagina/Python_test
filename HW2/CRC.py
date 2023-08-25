import zlib

def crc32(fileName):
    '''
    Контрольная сумма файла CRC-32
    '''
    with open(fileName, 'rb') as fh:
        hash = 0
        while True:
            s = fh.read(65536)
            if not s:
                break
            hash = zlib.crc32(s, hash)

        return "%08X" % (hash & 0xFFFFFFFF)