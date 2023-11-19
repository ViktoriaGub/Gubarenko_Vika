input_file_path = "C:\Users\Admin\Desktop\Губаренко Вика\#Задание 10\Губаренко_Виктория_Витальевна_У-234_vvod.txt"
output_file_path = "C:\Users\Admin\Desktop\Губаренко Вика\#Задание 10\Губаренко_Виктория_Витальевна_У-234_vivod.txt"
with open(input_file_path, 'r', encoding='utf-8') as file_in, open(output_file_path, 'w', encoding='utf-8') as file_out:
    for line in file_in:
        file_out.write(processed_data + '\n')
