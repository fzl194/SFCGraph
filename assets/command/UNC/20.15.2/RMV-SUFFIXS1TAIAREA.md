---
id: UNC@20.15.2@MMLCommand@RMV SUFFIXS1TAIAREA
type: MMLCommand
name: RMV SUFFIXS1TAIAREA（删除UPF服务区名称以TAC后缀方式绑定的S1TAI范围）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SUFFIXS1TAIAREA
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- TAC后缀绑定UP区域
status: active
---

# RMV SUFFIXS1TAIAREA（删除UPF服务区名称以TAC后缀方式绑定的S1TAI范围）

## 功能

**适用NF：SGW-C、PGW-C**

删除UPF服务区名称以TAC后缀方式绑定的S1TAI范围。

## 注意事项

- 该命令执行后立即生效。

- 当执行命令时不输入S1BEGINTAI参数时，会删除相同AREANAME、MCC、MNC、AREACODE下绑定的所有S1TAI范围。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为S1TAI。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于标识移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：无 |
| AREACODE | 区号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定的后缀区号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：<br>与S1BEGINTAC/S1ENDTAC拼接所得的十进制数应小于等于65535。 |
| S1BEGINTAC | TAC范围起始值 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF服务区名称绑定S1TAC范围起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：<br>Tac范围的结束值需要不小于Tac范围的开始值，且结束值和开始值长度需相等。与AREACODE参数拼接所得的十进制数应小于等于65535。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SUFFIXS1TAIAREA]] · UPF服务区名称以TAC后缀方式绑定的S1TAI范围（SUFFIXS1TAIAREA）

## 使用实例

删除UPF服务区名称为“UPAREA1”的以TAC后缀方式绑定的S1TAI范围，将移动国家码设置为“460”，将移动网号设置为“01”，将TAC范围起始值设置为“000”，将区号设置为“11”：

```
RMV SUFFIXS1TAIAREA: AREANAME="UPAREA1", MCC="460", MNC="01", AREACODE="11", S1BEGINTAC="000";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SUFFIXS1TAIAREA.md`
