def process_numbers(numbers):
    """
    处理整数列表并返回统计信息
    :param numbers: 整数列表
    :return: (平均值, 最大值, 最小值, 偶数和)
    """
    if not numbers:  
        return 0.0, 0, 0, 0
    
    avg = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    even_sum = sum(x for x in numbers if x % 2 == 0)
    
    return round(avg, 2), max_val, min_val, even_sum

def task1_main():
    print("请输入一系列整数，用逗号分隔（例如：1,2,3,4,5）")
    
    try:
        user_input = input(">>> ").strip().replace('，', ',')
        numbers = [int(num.strip()) for num in user_input.split(',')]
        average, maximum, minimum, even_total = process_numbers(numbers)
        
        print("\n处理结果：")
        print(f"平均值: {average}")
        print(f"最大值: {maximum}")
        print(f"最小值: {minimum}")
        print(f"偶数和: {even_total}")
        
    except ValueError:
        print("错误：请输入有效的整数（如 1,2,3）！")
    except Exception as e:
        print(f"发生未知错误: {e}")

if __name__ == "__main__":
    task1_main()
