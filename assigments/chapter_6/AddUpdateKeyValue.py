class HashItem():
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f'{{{self.key}: {self.value}}}'


class HashTable():
    def __init__(self, size=256):
        self.size = size
        self.slots = [None] * size
        self.used_slots = 0

    def __repr__(self):
        text = ''
        for index, slot in enumerate(self.slots):
            if slot:
                text += f', {index}: {slot}'
        plural = '' if self.used_slots == 1 else 's'
        return f'<HashTable ({self.used_slots} element{plural}): [{text.lstrip(", ")}]'

    def _hash(self, key):
        """
        Hashing function. Can be changed for a custom one.
        """
        # return len(key) % self.size
        return sum((index + 1) * ord(char) * ord(char) for index, char in enumerate(key)) % self.size

    def _find_free_slot(self, start):
        """
        Starting from 'start' find the next free slot available.

        Parameters:
        - 'start': Starting point for the search.

        Returns: The index of the next free slot or None if no free slots
        """
        # Start to search from the given position
        current = start

        # While that position is in use, enter the loop
        while self.slots[current]:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size

            # If we reach again the given position, that means
            # a whole cycle has been completed and there was no free
            # positions available
            if current == start:
                return None

        # After the loop, current points to a free position
        return current

    def _find_key(self, start, key):
        """
        Starting from 'start' try to find 'key'.

        Parameters:
        - 'start': Starting index
        - 'key': The key to be found

        Returns: The index position of the key or None if not found
        """
        # Start to search from the given position
        current = start

        # While current position is occupaid and it's not the key, enter the loop
        while self.slots[current] and self.slots[current].key != key:
            # Increment current, but if the end or the table is reached,
            # continue from the start of the table.
            current = (current + 1) % self.size
            # If we reach again the given position, that means
            # a whole cycle has been completed and the key was not found
            if current == start:
                return None

        # After the loop, current points to a free position or
        # to the position with the key
        if self.slots[current]:
            return current
        else:
            return None

    def put(self, key, value):
        """
        Add or updates a key with a value in the hash table

        Parameters:
        - 'key': The key to add or update.
        - 'value': The value of the key

        Returns: None
        """
        hash = self._hash(key)

        position = self._find_key(hash, key)

        if position is None:
            position = self._find_free_slot(hash)
            if position is None:
                raise MemoryError("No free slots available")
            self.used_slots += 1

        self.slots[position] = HashItem(key, value)


def test_find_free_slot1():
    h = HashTable()

    try:
        for i in range(257):
            h.put(f"key{i}", i)
    except MemoryError:
        pass

    print(h.slots)
    assert h.slots == "[{key80: 80}, {key112: 112}, {key26: 26}, {key69: 69}, {key98: 98}, {key108: 108}, {key203: 203}, {key230: 230}, {key181: 181}, {key229: 229}, {key239: 239}, {key43: 43}, {key240: 240}, {key243: 243}, {key2: 2}, {key20: 20}, {key44: 44}, {key73: 73}, {key42: 42}, {key74: 74}, {key87: 87}, {key162: 162}, {key72: 72}, {key39: 39}, {key178: 178}, {key200: 200}, {key102: 102}, {key45: 45}, {key186: 186}, {key199: 199}, {key219: 219}, {key75: 75}, {key247: 247}, {key231: 231}, {key58: 58}, {key27: 27}, {key41: 41}, {key135: 135}, {key184: 184}, {key71: 71}, {key145: 145}, {key221: 221}, {key241: 241}, {key249: 249}, {key125: 125}, {key250: 250}, {key253: 253}, {key172: 172}, {key255: 255}, {key251: 251}, {key46: 46}, {key236: 236}, {key209: 209}, {key137: 137}, {key76: 76}, {key99: 99}, {key147: 147}, {key155: 155}, {key211: 211}, {key226: 226}, {key127: 127}, {key115: 115}, {key4: 4}, {key40: 40}, {key88: 88}, {key191: 191}, {key7: 7}, {key70: 70}, {key188: 188}, {key133: 133}, {key157: 157}, {key224: 224}, {key143: 143}, {key234: 234}, {key244: 244}, {key216: 216}, {key123: 123}, {key117: 117}, {key28: 28}, {key13: 13}, {key130: 130}, {key165: 165}, {key14: 14}, {key47: 47}, {key140: 140}, {key153: 153}, {key12: 12}, {key59: 59}, {key77: 77}, {key105: 105}, {key120: 120}, {key63: 63}, {key167: 167}, {key113: 113}, {key64: 64}, {key15: 15}, {key150: 150}, {key182: 182}, {key62: 62}, {key194: 194}, {key196: 196}, {key201: 201}, {key206: 206}, {key11: 11}, {key107: 107}, {key110: 110}, {key214: 214}, {key65: 65}, {key163: 163}, {key175: 175}, {key204: 204}, {key33: 33}, {key228: 228}, {key238: 238}, {key34: 34}, {key61: 61}, {key89: 89}, {key139: 139}, {key16: 16}, {key32: 32}, {key103: 103}, {key149: 149}, {key160: 160}, {key198: 198}, {key129: 129}, {key177: 177}, {key48: 48}, {key35: 35}, {key218: 218}, {key222: 222}, {key1: 1}, {key10: 10}, {key29: 29}, {key66: 66}, {key78: 78}, {key31: 31}, {key100: 100}, {key159: 159}, {key232: 232}, {key212: 212}, {key242: 242}, {key119: 119}, {key6: 6}, {key60: 60}, {key93: 93}, {key173: 173}, {key94: 94}, {key192: 192}, {key208: 208}, {key131: 131}, {key36: 36}, {key17: 17}, {key92: 92}, {key141: 141}, {key170: 170}, {key185: 185}, {key121: 121}, {key169: 169}, {key246: 246}, {key95: 95}, {key248: 248}, {key252: 252}, {key3: 3}, {key30: 30}, {key67: 67}, {key151: 151}, {key202: 202}, {key91: 91}, {key109: 109}, {key136: 136}, {key146: 146}, {key187: 187}, {key254: 254}, {key111: 111}, {key126: 126}, {key53: 53}, {key134: 134}, {key235: 235}, {key54: 54}, {key49: 49}, {key144: 144}, {key245: 245}, {key52: 52}, {key37: 37}, {key79: 79}, {key96: 96}, {key124: 124}, {key156: 156}, {key161: 161}, {key179: 179}, {key183: 183}, {key55: 55}, {key116: 116}, {key154: 154}, {key9: 9}, {key18: 18}, {key90: 90}, {key180: 180}, {key225: 225}, {key51: 51}, {key101: 101}, {key114: 114}, {key215: 215}, {key83: 83}, {key227: 227}, {key195: 195}, {key68: 68}, {key84: 84}, {key138: 138}, {key166: 166}, {key82: 82}, {key148: 148}, {key233: 233}, {key237: 237}, {key56: 56}, {key97: 97}, {key128: 128}, {key164: 164}, {key106: 106}, {key23: 23}, {key85: 85}, {key171: 171}, {key24: 24}, {key158: 158}, {key197: 197}, {key217: 217}, {key5: 5}, {key22: 22}, {key38: 38}, {key50: 50}, {key81: 81}, {key104: 104}, {key118: 118}, {key132: 132}, {key142: 142}, {key25: 25}, {key189: 189}, {key193: 193}, {key122: 122}, {key176: 176}, {key205: 205}, {key213: 213}, {key86: 86}, {key21: 21}, {key207: 207}, {key210: 210}, {key168: 168}, {key19: 19}, {key57: 57}, {key152: 152}, {key174: 174}, {key190: 190}, {key220: 220}, {key223: 223}, {key0: 0}, {key8: 8}]"


test_find_free_slot1()