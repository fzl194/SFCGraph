---
id: UNC@20.15.2@MMLCommand@ADD SUFFIXLAIAREA
type: MMLCommand
name: ADD SUFFIXLAIAREA（增加UPF服务区名称以LAC后缀方式绑定的LAI范围）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: SUFFIXLAIAREA
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP跟踪区管理
- LAC后缀绑定UP区域
status: active
---

# ADD SUFFIXLAIAREA（增加UPF服务区名称以LAC后缀方式绑定的LAI范围）

## 功能

**适用NF：GGSN**

该命令用于增加UPF服务区名称以LAC后缀方式绑定的LAI范围。

## 注意事项

- 该命令执行后立即生效。

- 通过UPAREABINDLAI/SUFFIXLAIAREA配置的各UPF服务区名称绑定的LAI范围不允许出现交集。
- 设置了本命令后，不建议配置PNFTAIRANGE、LOCBINDLAI。
- 该命令需在UPAREABINDFUNC命令配置为SUFFIX或BOTH才可以下发。

- 最多可输入16384条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | UPF服务区名称 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>该参数取值应与命令LST UPAREA查询结果中的AREANAME保持一致；且该AREANAME在命令LST UPAREA查询结果中对应的AREATYPE取值应为LAI。 |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于标识移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识移动网号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：无 |
| BEGINLAC | LAC范围起始值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定LAC范围起始值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：<br>Lac范围的结束值需要不小于Lac范围的开始值，且结束值和开始值长度需相等。与AREACODE参数拼接所得的十进制数应小于等于65535。 |
| ENDLAC | LAC范围结束值 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定LAI范围结束值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：<br>Lac范围的结束值需要不小于Lac范围的开始值，且结束值和开始值长度需相等。与AREACODE参数拼接所得的十进制数应小于等于65535。 |
| AREACODE | 区号 | 可选必选说明：必选参数<br>参数含义：该参数用于标识UPF服务区名称绑定的后缀区号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是2。只允许输入十进制数字（0~9）。<br>默认值：无<br>配置原则：<br>与BEGINLAC/ENDLAC参数拼接所得的十进制数应小于等于65535。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SUFFIXLAIAREA]] · UPF服务区名称以LAC后缀方式绑定的LAI范围（SUFFIXLAIAREA）

## 使用实例

增加UPF服务区名称为“UPAREA1”以LAC后缀方式绑定的LAI范围，将移动国家码设置为“460”，移动网号设置为“01”，LAC范围设置为“000”~“111”，区号设置为“11”，如下设置完成后，会将4600100011、4600100111、4600100211、...、4600111011、4600111111与“UPAREA1”绑定：

```
ADD SUFFIXLAIAREA: AREANAME="UPAREA1", MCC="460", MNC="01", BEGINLAC="000", ENDLAC="111", AREACODE="11";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加UPF服务区名称以LAC后缀方式绑定的LAI范围（ADD-SUFFIXLAIAREA）_23782742.md`
