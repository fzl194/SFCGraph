# ConfigTask/builder/constants.py
"""ConfigTask 抽取 pipeline 常量。"""

# 实例键模板（对齐命令图谱 @ObjectType@ 风格）
ID_TMPL = "{nf}@{version}@ConfigTask@{seq:05d}"                       # task_id
CMD_REF_TMPL = "{nf}@{version}@MMLCommand@{name}"                    # command_ref
PARAM_REF_TMPL = "{nf}@{version}@CommandParameter@{cmd}:{param}"     # parameter_ref

# 状态/分类
STATUS_ACTIVE = "active"
CATEGORY_CONFIG = "配置"

# 配置类文档文件名前缀（csv_loader 过滤用）
CONFIG_DOC_PREFIXES = ("部署", "激活", "配置")

# md 4 段标题（md_reader 用，严格统一）
SECTION_FLOW = "操作流程"
SECTION_STEPS = "操作步骤"
SECTION_EXAMPLE = "任务示例"
SECTION_DATA = "数据规划表"
