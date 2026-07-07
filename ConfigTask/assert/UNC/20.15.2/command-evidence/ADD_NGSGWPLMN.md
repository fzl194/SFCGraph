# 命令证据包：ADD NGSGWPLMN
> 原始命令 md：`output/UNC 20.15.2 产品文档(裸机容器) 05/OM参考/命令/UNC MML命令/业务服务管理/会话管理/计费管理/离线计费/SGW计费控制/SGW-C PLMN信息管理/增加SGW-C Home PLMN（ADD NGSGWPLMN）_70382289.md`
> 用该命令的特性数：1

## ② 命令真相（mml_commands.jsonl）
**功能**：**适用NF：SGW-C**

该命令用于增加运营商的SGW-C Home PLMN。
**notes（规格/上限→应投影 atom rule）**：
- - 该命令执行后立即生效。

- 若MCC相同，MNC有效长度为2位和MNC有效长度为3位的记录，前两位不允许相同。

- 最多可输入512条记录。

**参数真相表（代码解析）**：

| 参数 | 描述 | 数据来源 | 必选 | 默认 | 取值范围 |
|---|---|---|---|---|---|
| NOID | 运营商标识 | local_planned | required | 无 | 整数类型，取值范围为0。 |
| MCC | 移动国家码 | local_planned | required | 无 | 字符串类型，输入长度是3。只允许输入十进制数字（0-9）。 |
| MNC | 移动网号 | local_planned | required | 无 | 字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。 |
| DESC | 描述信息 | local_planned | optional | 无 | 字符串类型，输入长度范围是0~32。 |

## ③ 各特性的配置范式（代码从激活 md 抽取 + 原始上下文）

### WSFD-011201

**md：`WSFD-011201/配置离线计费方式（SGW-C）_02167102.md`**
- 数据规划表（该命令的参数行）：
  | **ADD NGSGWPLMN** | 运营商标识（NOID） | 0 | 固定取值 | （可选）配置SGW-C的Home PLMN。当PGW-C与SGW-C部署在同一台设备上：<br>- 期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效），当SGW-C用户的IMSI中的PLMN未匹配到**ADD NGSGWPLMN**配置时判断用户为漫游用户。<br>- 期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。 |
  | **ADD NGSGWPLMN** | 移动国家码（MCC） | 123 | 全网规划 | （可选）配置SGW-C的Home PLMN。当PGW-C与SGW-C部署在同一台设备上：<br>- 期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效），当SGW-C用户的IMSI中的PLMN未匹配到**ADD NGSGWPLMN**配置时判断用户为漫游用户。<br>- 期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。 |
  | **ADD NGSGWPLMN** | 移动网号（MNC） | 68 | 全网规 | （可选）配置SGW-C的Home PLMN。当PGW-C与SGW-C部署在同一台设备上：<br>- 期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效），当SGW-C用户的IMSI中的PLMN未匹配到**ADD NGSGWPLMN**配置时判断用户为漫游用户。<br>- 期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。 |
  | **ADD NGSGWPLMN** | 描述信息（DESC） | sgw homeplmn1 | 本端规划 | （可选）配置SGW-C的Home PLMN。当PGW-C与SGW-C部署在同一台设备上：<br>- 期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与**ADD NGPLMN**配置匹配判断为本地用户的用户生效），当SGW-C用户的IMSI中的PLMN未匹配到**ADD NGSGWPLMN**配置时判断用户为漫游用户。<br>- 期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。 |
- 任务示例脚本（该命令行）：
  `ADD NGSGWPLMN: NOID=0, MCC="123", MNC="68", DESC="sgw homeplmn1";`
- 操作步骤上下文（±2 行原文）：
  L64:
    >   > 针对同一个用户，不同属性下规划的计费方式要一致，否则用户计费会出错。例如，针对CC取值为NORMAL的本地用户，如果设置NORMAL用户进行离线计费，又设置本地用户进行在线计费，则最终用户计费将出错。
    > 2. **可选：**配置SGW-C的Home PLMN。
    >   **ADD NGSGWPLMN**
    >   > **说明**
    >   > 当PGW-C与SGW-C部署在同一台设备上，期望SGW-C和PGW-C对同一用户按照不同的漫游属性进行计费时，可以通过该命令单独配置SGW-C的Home PLMN用于判断用户的漫游属性（仅对IMSI与 **ADD NGPLMN** 配置匹配判断为本地用户的用户生效）。期望SGW-C和PGW-C对同一用户按照相同的漫游属性进行计费时，不需要配置该命令。
  L142:
    > 
    > ```
    > ADD NGSGWPLMN: NOID=0, MCC="123", MNC="68", DESC="sgw homeplmn1";
    > ```

## ④ 自动比对
- 命令真相参数（4）：['DESC', 'MCC', 'MNC', 'NOID']
- atom 未建（pre-build 模式）；建 atom 时按真相 + ③ 范式决定绑定集
- 各特性数据规划表"获取方法"列分布：{'固定取值': 1, '全网规划': 1, '全网规': 1, '本端规划': 1}（多值→atom 应考虑 decision_driven）
