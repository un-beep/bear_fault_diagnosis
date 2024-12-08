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
            "IR014_3": 'https://engineering.case.edu/sites/default/files/177.mat',  #本文采用IR007_3数据
        },

        "Ball":{
            "B014_0": 'https://engineering.case.edu/sites/default/files/189.mat',
            "B014_1": 'https://engineering.case.edu/sites/default/files/190.mat',
            "B014_2": 'https://engineering.case.edu/sites/default/files/191.mat',
            "B014_3": 'https://engineering.case.edu/sites/default/files/192.mat',  #本文采用B007_3数据
        },

        "Outer_Race_Centered":{
                "OR014_6_0": 'https://engineering.case.edu/sites/default/files/109.mat',
                "OR014_6_1": 'https://engineering.case.edu/sites/default/files/110.mat',
                "OR014_6_2": 'https://engineering.case.edu/sites/default/files/111.mat',
                "OR014_6_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

    },

    "021inch":{
        "Inner_Race":{
            "IR021_0": 'https://engineering.case.edu/sites/default/files/109.mat',
            "IR021_1": 'https://engineering.case.edu/sites/default/files/110.mat',
            "IR021_2": 'https://engineering.case.edu/sites/default/files/111.mat',
            "IR021_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

        "Ball":{
            "B021_0": 'https://engineering.case.edu/sites/default/files/122.mat',
            "B021_1": 'https://engineering.case.edu/sites/default/files/123.mat',
            "B021_2": 'https://engineering.case.edu/sites/default/files/124.mat',
            "B021_3": 'https://engineering.case.edu/sites/default/files/125.mat',  #本文采用B007_3数据
        },

        "Outer_Race_Centered":{
                "OR021_6_0": 'https://engineering.case.edu/sites/default/files/109.mat',
                "OR021_6_1": 'https://engineering.case.edu/sites/default/files/110.mat',
                "OR021_6_2": 'https://engineering.case.edu/sites/default/files/111.mat',
                "OR021_6_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

        "Outer_Race_Orthogonal":{
                "OR021_3_0": 'https://engineering.case.edu/sites/default/files/109.mat',
                "OR021_3_1": 'https://engineering.case.edu/sites/default/files/110.mat',
                "OR021_3_2": 'https://engineering.case.edu/sites/default/files/111.mat',
                "OR021_3_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

        "Outer_Race_Opposite":{
                "OR021_12_0": 'https://engineering.case.edu/sites/default/files/109.mat',
                "OR021_12_1": 'https://engineering.case.edu/sites/default/files/110.mat',
                "OR021_12_2": 'https://engineering.case.edu/sites/default/files/111.mat',
                "OR021_12_3": 'https://engineering.case.edu/sites/default/files/112.mat',  #本文采用IR007_3数据
        },

    },


}


# 存储路径
paths = { './data/Normal_Baseline_Data',
          './data/48k_Drive_End_Bearing_Fault_Data/0.007inch',
          './data/48k_Drive_End_Bearing_Fault_Data/0.014inch',
          './data/48k_Drive_End_Bearing_Fault_Data/0.021inch',
}

# 确保目标文件夹存在
for path in paths:
    os.makedirs(path, exist_ok=True)

# 下载并保存文件
for normal_url, url in normal_urls.items():
    try:
        response = requests.get(url)
        response.raise_for_status()  # 如果请求失败，会抛出异常
        path_name = os.path.join(path, f"{normal_url}.mat")
        
        # 以二进制模式写入文件
        with open(path_name, 'wb') as f:
            f.write(response.content)
        print(f"文件 {normal_url}.mat 下载成功！")
        
    except requests.exceptions.RequestException as e:
        print(f"下载 {normal_url} 时发生错误: {e}")
