from adt import String


class MyString(String):

    def __init__(self, char_array):
        self.char_array = char_array

    def length(self) -> int:
        return len(self.char_array)

    def char_at(self, index: int) -> chr:
        if 0 <= index < self.length():
            return self.char_array[index]

    def concat(self, string: String):
        new_char_array = [None] * (self.length() + string.length())
        for i in range(self.length()):
            new_char_array[i] = self.char_at(i)
        for j in range(string.length()):
            new_char_array[self.length() + j] = string.char_at(j)
        return MyString(new_char_array)

    def ends_with(self, sub_string: String) -> bool:
        if sub_string.length() > self.length():
            return False

        if self.equals(sub_string):
            return True
        # a b c, 3
        #   b c, 2
        diff = self.length() - sub_string.length()

        for i in range(sub_string.length()):
            if self.char_at(diff + i) != sub_string.char_at(i):
                return False

        return True

    def starts_with(self, sub_string: String) -> bool:
        if sub_string.length() > self.length():
            return False

        if self.equals(sub_string):
            return True
            # a b c, 3
            #   b c, 2
        for i in range(sub_string.length()):
            if self.char_at(i) != sub_string.char_at(i):
                return False

        return True

    def equals(self, string: String) -> bool:
        is_equal = True
        if self.length() != string.length():
            is_equal = False
            return is_equal
        else:
            length = self.length()
            for i in range(length):
                if self.char_at(i) != string.char_at(i):
                    is_equal = False
        return is_equal

    # Find the starting index of a substring
    def index_of(self, string: String) -> int:
        pass

    def sub_string(self, i: int, j: int):

        if i < 0 or j >= self.length() or i > j:
            return MyString([])
        else:
            length = j - i + 1
            new_char_array = [None] * length
            char_index = 0
            for index in range(i, j+1):
                new_char_array[char_index] = self.char_at(index)
                char_index += 1
            return MyString(new_char_array)

    def append(self, substring: String):
        return self.insert(self.length(), substring)

    # Insert a substring staring at i
    def insert(self, index: int, sub_string: String):

        if index > self.length():
            pass

        new_l = (self.length() + sub_string.length())
        new_array = [None] * new_l
        # Move the space for new substring
        origin_index = 0
        sub_index = 0
        for i in range(new_l):
            if i < index:
                new_array[i] = self.char_array[origin_index]
                origin_index += 1
            elif index <= i < index + sub_string.length():
                new_array[i] = sub_string.char_at(sub_index)
                sub_index += 1
            else:
                new_array[i] = self.char_array[origin_index]
                origin_index += 1
        self.char_array = new_array
        return MyString(new_array)

    def reverse(self):
        size = self.length()
        if self.length() == 1:
            pass
        mid_index = int(size / 2)
        last_index = size - 1
        for i in range(mid_index):
            temp = self.char_at(i)
            self.set_char(i, self.char_at(last_index - i))
            self.set_char(last_index - i, temp)

    def set_char(self, index, char: chr):
        self.char_array[index] = char

    def print(self):
        for char in self.char_array:
            print(char, end="")
        print(" ")


def simple_testing():
    string1 = MyString(['a', 'b', 'c', 'd'])
    string2 = MyString(['b', 'c', 'd'])
    string3 = MyString(['b', 'c', 'd', 'a'])
    string4 = MyString(['a', 'd', 'd', 'a'])
    string5 = MyString(['a', 'd'])
    string6 = MyString(['a', 'd', 'c', 'd', 'a'])

    # Check equals
    print(string1.equals(string1))
    print(string1.equals(string2))
    print(string1.equals(string3))
    print(string1.equals(string4))
    print(string1.equals(string6))

    # Test reverse
    string1.reverse()
    string1.print()

    string2.reverse()
    string2.print()

    string5.reverse()
    string5.print()

    string6.reverse()
    string6.print()

    new_string = string3.concat(string4)
    new_string.print()


def suffix_testing():
    string1 = MyString(['a', 'b', 'c', 'd'])
    string2 = MyString(['a', 'b', 'd'])
    string3 = MyString(['c', 'd'])
    string4 = MyString(['b', 'c', 'd'])
    string5 = MyString(['a'])
    string6 = MyString(['a', 'b'])

    print("Test end with")
    print(string1.ends_with(string1))
    print(string1.ends_with(string2))
    print(string1.ends_with(string3))
    print(string1.ends_with(string4))
    print("Test start with")
    print(string1.starts_with(string1))
    print(string1.starts_with(string2))
    print(string1.starts_with(string3))
    print(string1.starts_with(string4))
    print(string1.starts_with(string5))
    print(string1.starts_with(string6))


def sub_string_test():
    string1 = MyString(['a', 'b', 'c', 'd', 'e'])
    sub1 = string1.sub_string(0, 1)
    sub1.print()
    sub1 = string1.sub_string(1, 4)
    sub1.print()
    sub1 = string1.sub_string(3, 4)
    sub1.print()
    sub1 = string1.sub_string(0, 5)
    sub1.print()
    sub1 = string1.sub_string(2, 3)
    sub1.print()
    sub1 = string1.sub_string(2, 2)
    sub1.print()

def insert_testing():
    string1 = MyString(['a', 'b', 'c', 'd', 'e'])
    sub_string = MyString(['g', 'q', 'h'])
    new_string = string1.insert(1, sub_string)
    new_string.print()
    string1 = MyString(['a', 'b', 'c', 'd', 'e'])
    string1.insert(0, sub_string)
    string1.print()
    string1 = MyString(['a', 'b', 'c', 'd', 'e'])
    string1.insert(5, sub_string)
    string1.print()
    string1 = MyString(['a', 'b', 'c', 'd', 'e'])
    string1.append(sub_string)
    string1.print()

#suffix_testing()
#sub_string_test()
#insert_testing()