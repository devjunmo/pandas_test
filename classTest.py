import pandas as pd


test_val = "classTest.py에 있는 변수"

class JustTest:

    class_attr = 5
    class_list = [0, ]


    def __init__(self, setInt, my_df):
        self.myInt = setInt
        self.myInt = JustTest.__myIntMult(self.myInt)
        inst_attr = 10
        self.instAttr = inst_attr

        # my_list = [0 for i in range(31)]
        # my_df["new_col"] = my_list # call by reference

        my_df.drop(['name'], axis=1, inplace=True)


    @staticmethod
    def __myIntMult(myInt): # 객체 점으로 안보이게
        my = myInt *10
        return my

    @staticmethod
    def lst_ones_plus(lst):
        lst[0] += 100
        JustTest.class_list[0] = lst[0]
        print(f"클래스 리스트는... {JustTest.class_list}")

        JustTest.class_list.clear()

    # @classmethod
    # def class_mtd_test(cls, lst):
    #     JustTest.class_list[0] = lst[0]


