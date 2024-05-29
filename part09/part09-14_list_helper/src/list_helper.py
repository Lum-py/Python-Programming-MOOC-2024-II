# WRITE YOUR SOLUTION HERE:
class ListHelper:
    @classmethod
    def greatest_frequency(cls, my_list: list):
        max = 0
        for i in my_list:
            count = my_list.count(i)
            if count > max:
                max = count
                common = i
        return common

    @classmethod
    def doubles(cls, my_list: list):
        single = []
        double = []
        for i in my_list:
            if i in single:
                if i not in double:
                    double.append(i)
            single.append(i)
        return len(double)



if __name__ == "__main__":
    numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print(ListHelper.greatest_frequency(numbers))
    print(ListHelper.doubles(numbers))