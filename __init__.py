# PORTRAIT MASTER
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.5
# https://stefanoflore.it
# https://ai-wiz.art

# 汉化 + 优化为读取json文件：Zho

import json
import os

def read_json_file(file_path):
    try:
        # Open file, load JSON content into python dictionary, and return it.
        with open(file_path, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            return json_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def get_name(json_data):
    # Check that data is a list
    if not isinstance(json_data, list):
        print("Error: input data must be a list")
        return None

    names = []

    # Iterate over each item in the data list
    for item in json_data:
        # Check that the item is a dictionary
        if isinstance(item, dict):
            # Check that 'name' is a key in the dictionary
            if 'name' in item:
                # Append the value of 'name' to the names list
                names.append(item['name'])

    return names

def get_prompt(json_data, template_name):
    try:
        # Check if json_data is a list
        if not isinstance(json_data, list):
            raise ValueError("Invalid JSON data. Expected a list of templates.")
            
        for template in json_data:
            # Check if template contains 'name' and 'prompt' fields
            if 'name' not in template or 'prompt' not in template:
                raise ValueError("Invalid template. Missing 'name' or 'prompt' field.")
            
            if template['name'] == template_name:
                prompt = template.get('prompt', "")
                print("Extracted prompt:", prompt)
                return prompt

        # If function hasn't returned yet, no matching template was found
        raise ValueError(f"No template found with name '{template_name}'.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


class PortraitMaster_中文版:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(self):
        # Get current file's directory
        p = os.path.dirname(os.path.realpath(__file__))

        # Paths for various JSON files
        shot_file_path = os.path.join(p, 'lists/shot_list.json')
        gender_file_path = os.path.join(p, 'lists/gender_list.json')
        face_shape_file_path = os.path.join(p, 'lists/face_shape_list.json')
        facial_expressions_file_path = os.path.join(p, 'lists/face_expression_list.json')
        nationality_file_path = os.path.join(p, 'lists/nationality_list.json')
        hair_style_file_path = os.path.join(p, 'lists/hair_style_list.json')

        # Read JSON from file
        self.shot_data = read_json_file(shot_file_path)
        self.gender_data = read_json_file(gender_file_path)
        self.face_shape_data = read_json_file(face_shape_file_path)
        self.facial_expressions_data = read_json_file(facial_expressions_file_path)
        self.nationality_data = read_json_file(nationality_file_path)
        self.hair_style_data = read_json_file(hair_style_file_path)

        # Retrieve name from JSON data
        shot_list = get_name(self.shot_data)
        shot_list = ['-'] + shot_list
        gender_list = get_name(self.gender_data)
        gender_list = ['-'] + gender_list
        face_shape_list = get_name(self.face_shape_data)
        face_shape_list = ['-'] + face_shape_list
        facial_expressions_list = get_name(self.facial_expressions_data)
        facial_expressions_list = ['-'] + facial_expressions_list
        nationality_list = get_name(self.nationality_data)
        nationality_list = ['-'] + nationality_list
        hair_style_list = get_name(self.hair_style_data)
        hair_style_list = ['-'] + hair_style_list
        
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
                    "default": 1,
                    "step": 0.05,
                    "min": 0,
                    "max": max_float_value,
                    "display": "slider",
                }),
                "面部对称性": ("FLOAT", {
                    "default": 0.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "发型": (hair_style_list, {
                    "default": hair_style_list[0],
                }),
                "头发蓬松度": ("FLOAT", {
                    "default": 1,
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
                    "default": 0.5,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "皮肤毛孔": ("FLOAT", {
                    "default": 0.3,
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
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "虹膜细节": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形虹膜": ("FLOAT", {
                    "default": 1.2,
                    "min": 0,
                    "max": max_float_value,
                    "step": 0.05,
                    "display": "slider",
                }),
                "圆形瞳孔": ("FLOAT", {
                    "default": 1.2,
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
                    "default": "(white background:1.5)"
                }),
                "结束提示词": ("STRING", {
                    "multiline": True,
                    "default": ""
                }),
            }
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "pm"
    CATEGORY = "📸肖像大师"

    def pm(self, 镜头类型="-", 镜头权重=1, 性别="-", 面部表情="-", 面部表情权重=0, 脸型="-", 脸型权重=0, 国籍_1="-", 国籍_2="-", 国籍混合=0.5, 年龄=20, 发型="-", 头发蓬松度=0, 酒窝=0, 雀斑=0, 皮肤毛孔=0, 皮肤细节=0, 痣=0, 皮肤瑕疵=0, 眼睛细节=1, 虹膜细节=1, 圆形虹膜=1, 圆形瞳孔=1, 面部对称性=0, 补充提示词="", 起始提示词="", 结束提示词=""):

        shot = get_prompt(self.shot_data, 镜头类型)
        gender = get_prompt(self.gender_data, 性别)
        face_shape = get_prompt(self.face_shape_data, 脸型)
        facial_expressions = get_prompt(self.facial_expressions_data, 面部表情)
        nationality_1 = get_prompt(self.nationality_data, 国籍_1)
        nationality_2 = get_prompt(self.nationality_data, 国籍_2)
        hair_style = get_prompt(self.hair_style_data, 发型)

        prompt = []

        if 性别 == "-":
            性别 = ""
        else:
            性别 = " " + gender + " "

        if 国籍_1 != '-' and 国籍_2 != '-':
            nationality_mix_diff = 1 - round(国籍混合, 2)
            Anationality = f"[{nationality_1}:{nationality_2}:{round(国籍混合, 2)}:{round(nationality_mix_diff, 2)}]"
        elif 国籍_1 != '-':
            Anationality = nationality_1 + " "
        elif 国籍_2 != '-':
            Anationality = nationality_2 + " "
        else:
            Anationality = ""

        if 起始提示词 != "":
            prompt.append(f"{起始提示词}")

        if 镜头类型 != "-":
            prompt.append(f"({shot}:{round(镜头权重, 2)})")

        prompt.append(f"{Anationality}{性别}{round(年龄)}-years-old")

        if 面部表情 != "-":
            prompt.append(f"({facial_expressions}, {facial_expressions} expression:{面部表情权重})")

        if 脸型 != "-":
            prompt.append(f"({face_shape} shape face:{脸型权重})")

        if 发型 != "-":
            prompt.append(f"({hair_style} hairstyle:1.25)")

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
