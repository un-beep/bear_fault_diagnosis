import requests
import os

# 文件下载的URLs
# 本论文只使用normal_3作为健康数据
Normal_Baseline_Data_URLs = {
    "normal_0": 'https://engineering.case.edu/sites/default/files/97.mat',
    "normal_1": 'https://engineering.case.edu/sites/default/files/98.mat',
    "normal_2": 'https://engineering.case.edu/sites/default/files/99.mat',
    "normal_3": 'https://engineering.case.edu/sites/default/files/100.mat',
}

# 使用48KHz采样率下的Motor Load (HP)3为故障数据集，外圈故障区域为6:00
Bearing_Fault_Data_URLs={
    "007inch":{
        "Inner_Race":{
            "IR007_0": 'https://engineering.case.edu/sites/default/files/109.mat',
            "IR007_1": 'https://engineering.case.edu/sites/default/files/110.mat',
            "IR007_2": 'https://engineering.case.edu/sites/default/files/111.mat',
            "IR007_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

        "Ball":{
            "B007_0": 'https://engineering.case.edu/sites/default/files/122.mat',
            "B007_1": 'https://engineering.case.edu/sites/default/files/123.mat',
            "B007_2": 'https://engineering.case.edu/sites/default/files/124.mat',
            "B007_3": 'https://engineering.case.edu/sites/default/files/125.mat',  #本文采用B007_3数据
        },

        "Outer_Race_Centered":{
                "OR007_6_0": 'https://engineering.case.edu/sites/default/files/135.mat',
                "OR007_6_1": 'https://engineering.case.edu/sites/default/files/136.mat',
                "OR007_6_2": 'https://engineering.case.edu/sites/default/files/137.mat',
                "OR007_6_3": 'https://engineering.case.edu/sites/default/files/138.mat',  #本文采用OR007_6_3数据
        },

        "Outer_Race_Orthogonal":{
                "OR007_3_0": 'https://engineering.case.edu/sites/default/files/148.mat',
                "OR007_3_1": 'https://engineering.case.edu/sites/default/files/149.mat',
                "OR007_3_2": 'https://engineering.case.edu/sites/default/files/150.mat',
                "OR007_3_3": 'https://engineering.case.edu/sites/default/files/151.mat', 
        },

        "Outer_Race_Opposite":{
                "OR007_12_0": 'https://engineering.case.edu/sites/default/files/161.mat',
                "OR007_12_1": 'https://engineering.case.edu/sites/default/files/162.mat',
                "OR007_12_2": 'https://engineering.case.edu/sites/default/files/163.mat',
                "OR007_12_3": 'https://engineering.case.edu/sites/default/files/164.mat', 
        },

    },

    "014inch":{
        "Inner_Race":{
            "IR014_0": 'https://engineering.case.edu/sites/default/files/174.mat',
            "IR014_1": 'https://engineering.case.edu/sites/default/files/175.mat',
            "IR014_2": 'https://engineering.case.edu/sites/default/files/176.mat',
            "IR014_3": 'https://engineering.case.edu/sites/default/files/177.mat',  #本文采用IR014_3数据
        },

        "Ball":{
            "B014_0": 'https://engineering.case.edu/sites/default/files/189.mat',
            "B014_1": 'https://engineering.case.edu/sites/default/files/190.mat',
            "B014_2": 'https://engineering.case.edu/sites/default/files/191.mat',
            "B014_3": 'https://engineering.case.edu/sites/default/files/192.mat',  #本文采用B014_3数据
        },

        "Outer_Race_Centered":{
                "OR014_6_0": 'https://engineering.case.edu/sites/default/files/201.mat',
                "OR014_6_1": 'https://engineering.case.edu/sites/default/files/202.mat',
                "OR014_6_2": 'https://engineering.case.edu/sites/default/files/203.mat',
                "OR014_6_3": 'https://engineering.case.edu/sites/default/files/204.mat',  #本文采用OR014_6_3数据
        },

    },

    "021inch":{
        "Inner_Race":{
            "IR021_0": 'https://engineering.case.edu/sites/default/files/213.mat',
            "IR021_1": 'https://engineering.case.edu/sites/default/files/214.mat',
            "IR021_2": 'https://engineering.case.edu/sites/default/files/215.mat',
            "IR021_3": 'https://engineering.case.edu/sites/default/files/217.mat',  #本文采用IR021_3数据
        },

        "Ball":{
            "B021_0": 'https://engineering.case.edu/sites/default/files/226.mat',
            "B021_1": 'https://engineering.case.edu/sites/default/files/227.mat',
            "B021_2": 'https://engineering.case.edu/sites/default/files/228.mat',
            "B021_3": 'https://engineering.case.edu/sites/default/files/229.mat',  #本文采用B021_3数据
        },

        "Outer_Race_Centered":{
                "OR021_6_0": 'https://engineering.case.edu/sites/default/files/238.mat',
                "OR021_6_1": 'https://engineering.case.edu/sites/default/files/239.mat',
                "OR021_6_2": 'https://engineering.case.edu/sites/default/files/240.mat',
                "OR021_6_3": 'https://engineering.case.edu/sites/default/files/241.mat',  #本文采用OR021_6_3数据
        },

        "Outer_Race_Orthogonal":{
                "OR021_3_0": 'https://engineering.case.edu/sites/default/files/250.mat',
                "OR021_3_1": 'https://engineering.case.edu/sites/default/files/251.mat',
                "OR021_3_2": 'https://engineering.case.edu/sites/default/files/252.mat',
                "OR021_3_3": 'https://engineering.case.edu/sites/default/files/253.mat',  
        },

        "Outer_Race_Opposite":{
                "OR021_12_0": 'https://engineering.case.edu/sites/default/files/262.mat',
                "OR021_12_1": 'https://engineering.case.edu/sites/default/files/263.mat',
                "OR021_12_2": 'https://engineering.case.edu/sites/default/files/264.mat',
                "OR021_12_3": 'https://engineering.case.edu/sites/default/files/265.mat',  
        },

    },


}


# 存储路径
paths = { 
            "Normal_Baseline_Data": './data/Normal_Baseline_Data',
            "0.007inch": './data/48k_Drive_End_Bearing_Fault_Data/0.007inch',
            "0.014inch": './data/48k_Drive_End_Bearing_Fault_Data/0.014inch',
            "0.021inch": './data/48k_Drive_End_Bearing_Fault_Data/0.021inch',
}
    

# 下载并保存文件
for type_name, path in paths.items():
    # 确保文件夹存在，不存在则创建文件夹
    os.makedirs(path, exist_ok=True)

    if path == './data/Normal_Baseline_Data':
        for Normal_Baseline_Data_Name, url in Normal_Baseline_Data_URLs.items():
            try:
                response = requests.get(url)
                response.raise_for_status()  # 如果请求失败，会抛出异常
                path_name = os.path.join(path, f"{Normal_Baseline_Data_Name}.mat")

                # 以二进制模式写入文件
                with open(path_name, 'wb') as f:
                    f.write(response.content)
                print(f"文件 {Normal_Baseline_Data_Name}.mat 下载成功！")

            except requests.exceptions.RequestException as e:
                print(f"下载 {Normal_Baseline_Data_Name} 时发生错误: {e}")

    for size_type, total_urls in Bearing_Fault_Data_URLs.items():
        for fault_type, urls in total_urls.items():
            # 根据故障位置分类保存到对应的文件夹内
            path = path + f"/{size_type}/{fault_type}/" 
            # 确保文件夹存在，不存在则创建文件夹
            os.makedirs(path, exist_ok=True)
            try:              
                for data_name, url in urls.items():
                    response = requests.get(url)
                    response.raise_for_status()  # 如果请求失败，会抛出异常
                    path_name = os.path.join(path, f"{data_name}.mat")

                    # 以二进制模式写入文件
                    with open(path_name, 'wb') as f:
                        f.write(response.content)
                    print(f"文件 {data_name}.mat 下载成功！")

            except requests.exceptions.RequestException as e:
                print(f"下载 {data_name} 时发生错误: {e}")
