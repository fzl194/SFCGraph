---
id: UNC@20.15.2@MMLCommand@ADD APNAREA
type: MMLCommand
name: ADD APNAREA（增加APN相关服务区域）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: APNAREA
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- APN相关服务区域管理
status: active
---

# ADD APNAREA（增加APN相关服务区域）

## 功能

**适用NF：SMF**

该命令用于增加APN相关服务区域。服务区域通常是企业园区所处的区域。在服务区域内，根据用户位置可以做APN粒度相关特性控制。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入16000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | APN相关服务区域 | 可选必选说明：必选参数<br>参数含义：该参数用于配置APN相关服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：无 |
| AREATYPE | APN服务区域类型 | 可选必选说明：必选参数<br>参数含义：该参数用于配置APN服务区域类型。<br>数据来源：全网规划<br>取值范围：<br>- “N2TAI（5G类型的TAI）”：5G类型的TAI<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [APN相关服务区域（APNAREA）](configobject/UNC/20.15.2/APNAREA.md)

## 使用实例

增加5G类型的TAI服务区域：

```
ADD APNAREA: AREANAME="dnnarea1", AREATYPE=N2TAI;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加APN相关服务区域（ADD-APNAREA）_49830741.md`
