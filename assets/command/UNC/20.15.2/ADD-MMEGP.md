---
id: UNC@20.15.2@MMLCommand@ADD MMEGP
type: MMLCommand
name: ADD MMEGP（增加MME群组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: MMEGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 64
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组配置
status: active
---

# ADD MMEGP（增加MME群组）

## 功能

**适用网元：MME**

此命令用于增加MME群组记录。MME群组用于定义一组MME组成的MME区域，以该区域为粒度进行业务策略控制。需要结合 [**ADD MMEGPMEM**](../MME群组成员配置/增加MME群组成员(ADD MMEGPMEM)_26305434.md) 命令为MME群组添加成员。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为64。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0～63<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：长度为2或3的十进制数<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME组识别码。<br>数据来源：全网规划<br>取值范围：4位16进制编码<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEGP]] · MME群组（MMEGP）

## 使用实例

增加一组 “MME群组索引” 为1， “移动国家码” 为“123”， “移动网号” 为“001”， “MME组识别码” 为 “0001” 的记录

ADD MMEGP: MMEGPIDX=1, MCC="123", MNC="001", MMEGI="0001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加MME群组(ADD-MMEGP)_72225301.md`
