# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.5
# https://stefanoflore.it
# https://ai-wiz.art

# 汉化：Zho

import os

script_dir = os.path.dirname(__file__)

# read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# setup vars

shot_list = pmReadTxt(os.path.join(script_dir, "lists/shot_list.txt"))
shot_list.sort()
shot_list = ['-'] + shot_list

gender_list = pmReadTxt(os.path.join(script_dir, "lists/gender_list.txt"))
gender_list.sort()
gender_list = ['-'] + gender_list

face_shape_list = pmReadTxt(os.path.join(script_dir, "lists/face_shape_list.txt"))
face_shape_list.sort()
face_shape_list = ['-'] + face_shape_list

facial_expressions_list = pmReadTxt(os.path.join(script_dir, "lists/face_expression_list.txt"))
facial_expressions_list.sort()
facial_expressions_list = ['-'] + facial_expressions_list

nationality_list = pmReadTxt(os.path.join(script_dir, "lists/nationality_list.txt"))
nationality_list.sort()
nationality_list = ['-'] + nationality_list

hair_style_list = pmReadTxt(os.path.join(script_dir, "lists/hair_style_list.txt"))
hair_style_list.sort()
hair_style_list = ['-'] + hair_style_list

class PortraitMaster_中文版:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        max_float_value = 1.75
        return {
            "required": {
                "镜头类型": (shot_list, {
                    "default": shot_list[0],
                }),
                "镜头权重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "性别": (gender_list, {
                    "default": gender_list[0],
                }),
                "国籍_1": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍_2": (nationality_list, {
                    "default": nationality_list[0],
                }),
                "国籍混合": ("FLOAT", {
                    "default": 0.5,
                    "min": 0,
                    "max": 1,
                    "step": 0.05,
                    "display": "slider",
                }),
                "面部表情": (facial_expressions_list, {
                    "default": facial_expressions_list[0],
                }),
                "面部表情权重": ("FLOAT", {
                    "default": 1.5,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "脸型": (face_shape_list, {
                    "default": face_shape_list[0],
                }),
                "脸型权重": ("FLOAT", {
                    "default": 0,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部对称性": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "发型": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "头发蓬松度": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "年龄": ("INT", {
                    "default": 20,
                    "min": 18,
                    "max": 90,
                    "step": 1,
                    "display": "slider",
                }),
                "皮肤细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤毛孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "酒窝": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "雀斑": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "痣": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤瑕疵": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "眼睛细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜细节": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形虹膜": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形瞳孔": ("FLOAT", {
                    "default": 0,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "起始提示词": ("STRING", {
                    "multiline": True,
                    "default": "raw photo, (realistic:1.5)"
                }),
                "补充提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
                "结束提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING",)

    FUNCTION = "pm"

    CATEGORY = "AI WizArt"

    def pm(self, 镜头类型="-", 镜头权重=1, 性别="-", 面部表情="-", 面部表情权重=0, 脸型="-", 脸型权重=0, 国籍_1="-", 国籍_2="-", 国籍混合=0.5, 年龄=20, 发型="-", 头发蓬松度=0, 酒窝=0, 雀斑=0, 皮肤毛孔=0, 皮肤细节=0, 痣=0, 皮肤瑕疵=0, 眼睛细节=1, 虹膜细节=1, 圆形虹膜=1, 圆形瞳孔=1, 面部对称性=0, 补充提示词="", 起始提示词="", 结束提示词=""):

        prompt = []

        if 性别 == "-":
            性别 = ""
        else:
            性别 = " " + 性别 + " "

        if 国籍_1 != '-' and 国籍_2 != '-':
            nationality_mix_diff = 1 - round(国籍混合, 2)
            nationality = f"[{国籍_1}:{国籍_2}:{round(国籍混合, 2)}:{round(nationality_mix_diff, 2)}]"
        elif 国籍_1 != '-':
            nationality = 国籍_1 + " "
        elif 国籍_2 != '-':
            nationality = 国籍_2 + " "
        else:
            nationality = ""

        if 起始提示词 != "":
            prompt.append(f"{起始提示词}")

        if 镜头类型 != "-":
            prompt.append(f"({镜头类型}:{round(镜头权重, 2)})")

        prompt.append(f"{nationality}{性别}{round(年龄)}-years-old")

        if 面部表情 != "-":
            prompt.append(f"({面部表情}, {面部表情} expression:{面部表情权重})")

        if 脸型 != "-":
            prompt.append(f"({脸型} shape face:{脸型权重})")

        if 发型 != "-":
            prompt.append(f"({发型} hairstyle:1.25)")

        if 头发蓬松度 != "-":
            prompt.append(f"(disheveled:{round(头发蓬松度, 2)})")

        if 补充提示词 != "":
            prompt.append(f"{补充提示词}")

        if 皮肤细节 > 0:
            prompt.append(f"(skin details, skin texture:{round(皮肤细节, 2)})")

        if 皮肤毛孔 > 0:
            prompt.append(f"(skin pores:{round(皮肤毛孔, 2)})")

        if 皮肤瑕疵 > 0:
            prompt.append(f"(skin imperfections:{round(皮肤瑕疵, 2)})")

        if 酒窝 > 0:
            prompt.append(f"(dimples:{round(酒窝, 2)})")

        if 雀斑 > 0:
            prompt.append(f"(freckles:{round(雀斑, 2)})")

        if 痣 > 0:
            prompt.append(f"(skin pores:{round(痣, 2)})")

        if 眼睛细节 > 0:
            prompt.append(f"(eyes details:{round(眼睛细节, 2)})")

        if 虹膜细节 > 0:
            prompt.append(f"(iris details:{round(虹膜细节, 2)})")

        if 圆形虹膜 > 0:
            prompt.append(f"(circular iris:{round(圆形虹膜, 2)})")

        if 圆形瞳孔 > 0:
            prompt.append(f"(circular pupil:{round(圆形瞳孔, 2)})")

        if 面部对称性 > 0:
            prompt.append(f"(facial asymmetry, face asymmetry:{round(面部对称性, 2)})")

        if 结束提示词 != "":
            prompt.append(f"{结束提示词}")

        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        print("Portrait Master as generate the prompt:")
        print(prompt)

        return (prompt,)
    
NODE_CLASS_MAPPINGS = {
    "PortraitMaster_中文版": PortraitMaster_中文版
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PortraitMaster_中文版": "肖像大师_中文版"
}
