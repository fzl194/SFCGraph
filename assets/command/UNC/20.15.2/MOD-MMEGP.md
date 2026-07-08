---
id: UNC@20.15.2@MMLCommand@MOD MMEGP
type: MMLCommand
name: MOD MMEGP（修改MME群组）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: MMEGP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 移动性管理
- MME群组管理
- MME群组配置
status: active
---

# MOD MMEGP（修改MME群组）

## 功能

**适用网元：MME**

该命令用于修改MME群组。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEGPIDX | MME群组索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MME群组索引。<br>数据来源：全网规划<br>取值范围：0～63<br>默认值：无 |
| MCC | 移动国家码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：3位十进制数<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定移动网号。<br>数据来源：全网规划<br>取值范围：位数为2或3的十进制数<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：可选参数<br>参数含义：该参数用于指定MME组识别码。<br>数据来源：全网规划<br>取值范围：4位16进制编码<br>默认值：无 |
| DESC | 描述信息 | 可选必选说明：可选参数<br>参数含义：该参数用于指定描述信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为0～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MMEGP]] · MME群组（MMEGP）

## 使用实例

修改 “MME群组索引” 为1， “移动国家码” 为“123”， “移动网号” 为“001”， “MME组识别码” 为 “0001” 的记录

MOD MMEGP: MMEGPIDX=1, MCC="123", MNC="001", MMEGI="0001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-MMEGP.md`
