import time
import hyper_n_Sanya
import hyper_n_Max


def main():
    start = time.perf_counter()

    num1 = 2
    num2 = 2
    grade = 5

    print("result1 =",hyper_n_Sanya.hyper_n(num1,num2,grade))
    print("result2 =",hyper_n_Max.hyperN(num1,num2,grade))


if __name__ == '__main__':
    main()
