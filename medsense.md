# medsense.md
## 介绍
大模型可以根据已有知识能够进行稳定正常的能力发挥，同时对于噪声数据能够有着较公正的应对，同时考虑到微调的专业大模型成本较高且准确率无法保证，这里在选择大模型的基础长加入了RAG技术，来增加模型的专业表述能力，为用户提供一个专业领域的问答助手

主要的技术有：

- xinference 管理和调用大模型（对话模型和嵌入模型），并提供用户管理的前端界面
- langchain 可视化用户交互界面 调用大模型api接口 知识库创建
## 功能说明
这里主要是提供不同类型用户的不同功能：
- 普通用户，提供一个基于RAG的对话窗口和一个意见反馈的界面
- 管理员用户，可以管理知识库，对知识库的文件进行增删，并且也可以设置具体知识库的参数，如：嵌入模型。
## 运行要求
两个python环境，这里使用anacondda，实现对环境的管理：
- xinference，python版本3.9
- chat，python版本3.9

### xinference启动
激活环境
`conda activate xinference`

启动框架
`xinference-loal`
### 主程序启动
激活环境
`conda activate chat`

在项目根路径,输入
`python chatchat/cli.py start -a`
# 完成时间
2024年11月20日