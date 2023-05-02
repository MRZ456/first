height = float(input("请输入身高(单位：m)："))
weight = float(input("请输入体重(单位：kg)："))
BMI = weight/(height**2)
if BMI > 32:
    print(f'君のBMI指数わ：{BMI:.2f}です 严重肥胖')
elif 28 < BMI <= 32:
    print(f'君のBMI指数わ：{BMI:.2F}です 肥胖')  
elif 24 < BMI <= 28:
    print(f'君のBMI指数わ：{BMI:.2f}です 过重')
elif 18.5 < BMI <= 24:
    print(f'君のBMI指数わ：{BMI:.2f}です 正常')
else:
    print(f'君のBMI指数わ：{BMI:.2f}です 过轻')               