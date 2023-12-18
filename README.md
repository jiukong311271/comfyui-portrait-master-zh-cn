# ComfyUI Portrait Master 简体中文版

![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/7b183c08-a95f-4464-9e51-979894cb2b60)

## 项目介绍 | Info

- 人物肖像提示词生成模块，优化肖像生成，选择永远比填空更适合人类！

- 优化 + 汉化 自 [ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git)

## 参数说明 | Parameters

- 镜头类型：头像、肩部以上肖像、半身像、全身像、脸部肖像
- 性别：女性、男性
- 国籍_1：193个国家可选
- 国籍_2：193个国家可选
- 面部表情：开心、伤心、生气、惊讶、害怕等24种
- 脸型：椭圆形、圆形、梨形等12种
- 发型：法式波波头、卷发波波头、不对称剪裁等20种
- 起始提示词：写在开头的提示词
- 补充提示词：写在中间用于补充信息的提示词
- 结束提示词：写在末尾的提示词

## 提示词合成顺序 | Prompt composition order

- 起始提示词
- 镜头类型 + 镜头权重
- 国籍 + 性别 + 年龄
- 面部表情 + 面部表情权重
- 脸型 + 脸型权重
- 发型
- 头发蓬松度
- 补充提示词
- 皮肤细节
- 皮肤毛孔
- 皮肤瑕疵
- 酒窝
- 雀斑
- 痣
- 眼睛细节
- 虹膜细节
- 圆形虹膜
- 圆形瞳孔
- 面部对称性
- 结束提示词

## 自定义 | Customizations

可将需要自定义增加的内容写到lists文件夹中对应的json文件里（如发型、表情等）

## 使用建议 | Practical advice

皮肤和眼睛细节等参数过高时可能会覆盖所选镜头的设置。在这种情况下，建议减小皮肤和眼睛的参数值，或者插入否定提示(closeup, close up, close-up:1.5)，并根据需要修改权重。

## 安装 | Install

1. `cd custom_nodes`
2. `git clone https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn.git`
3. 重启 ComfyUI

## 工作流 | Workflow

[SD1.5 or SDXL](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%E3%80%90Zho%E3%80%91.json)

![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/e1269817-36e6-4f20-92f6-7119128b65d4)


[SDXL Turbo（non-commercial）](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/blob/main/workflows/Portrait%20Master%20%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87%E7%89%88%20SDXL%20Turbo%E3%80%90Zho%E3%80%91.json)

![image](https://github.com/ZHO-ZHO-ZHO/comfyui-portrait-master-zh-cn/assets/140084057/459162f0-a079-42af-990b-e916f32a0ff7)


## 更新日志 | Changelog

20231218

- V2.0版，新增6项参数，扩充2项参数，优化代码：
    - 眼睛颜色（8种）
    - 头发颜色（9种）
    - 灯光类型（32种）
    - 灯光方向（10种）
    - 提高照片真实感
    - 负面提示词
    - 镜头类型（+3种）
    - 发型（+19种）

20231216

- 完成代码优化，将原本读取txt文件调整成读取json文件，更加方便使用、自定义和扩展

20231215

- 对 [ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git) 完成汉化

## Credits

[ComfyUI Portrait Master](https://github.com/florestefano1975/comfyui-portrait-master.git)


