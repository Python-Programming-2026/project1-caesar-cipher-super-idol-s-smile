# 凯撒密码工具：仅支持英文字母加密/解密，其他字符（数字、符号、空格）保持不变

def caesar_code(original_str, offset, is_encrypt):
    """
    凯撒密码加密/解密函数
    :param original_str: 要处理的原始文本（比如"Hello123"）
    :param offset: 偏移量（整数，比如3表示字母后移3位）
    :param is_encrypt: 是否加密（True=加密，False=解密）
    :return: 加密/解密后的文本
    """
    # 存储最终处理后的结果
    final_result = ""
    
    # 解密时，偏移量取反（加密移3位，解密就移-3位）
    if not is_encrypt:
        offset = -offset
    
    # 逐个处理文本里的每个字符
    for single_char in original_str:
        # 先判断是不是大写字母（A-Z）
        if single_char.isupper():
            # 1. 把大写字母转成0-25的数字（A=0，B=1...Z=25）
            char_num = ord(single_char) - ord('A')
            # 2. 按偏移量移动，%26保证数字不超出0-25（比如Z+3=25+3=28→28%26=2→对应C）
            new_char_num = (char_num + offset) % 26
            # 3. 把数字转回大写字母
            new_char = chr(new_char_num + ord('A'))
            # 4. 加到结果里
            final_result += new_char
        
        # 再判断是不是小写字母（a-z）
        elif single_char.islower():
            # 逻辑和大写字母一致，只是基准换成a
            char_num = ord(single_char) - ord('a')
            new_char_num = (char_num + offset) % 26
            new_char = chr(new_char_num + ord('a'))
            final_result += new_char
        
        # 不是字母（数字/符号/空格），直接保留
        else:
            final_result += single_char
    
    return final_result

if __name__ == "__main__":
    # 1. 提示选择加密/解密，做输入校验（避免输错）
    while True:
        operation = input("请选择操作：输入 加密 或 解密：").strip()
        if operation in ["加密", "解密"]:
            break
        else:
            print("输入错误！只能输入“加密”或“解密”，请重新输入。")
    
    # 2. 提示输入要处理的文本
    text = input("请输入要{}的文本：".format(operation)).strip()
    
    # 3. 提示输入偏移量，做输入校验（确保是整数）
    while True:
        offset_input = input("请输入偏移量（任意整数，比如3）：").strip()
        try:
            offset = int(offset_input)
            break
        except ValueError:
            print("输入错误！偏移量必须是整数，比如3、5、-2，请重新输入。")
    
    # 4. 调用函数处理文本
    if operation == "加密":
        result = caesar_code(text, offset, is_encrypt=True)
        print(f"加密结果为：{result}")
    else:
        result = caesar_code(text, offset, is_encrypt=False)
        print(f"解密结果为：{result}")