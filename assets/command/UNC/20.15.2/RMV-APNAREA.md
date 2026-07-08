---
id: UNC@20.15.2@MMLCommand@RMV APNAREA
type: MMLCommand
name: RMV APNAREA（删除APN相关服务区域）
nf: UNC
version: 20.15.2
verb: RMV
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

# RMV APNAREA（删除APN相关服务区域）

## 功能

**适用NF：SMF**

该命令用于删除APN相关服务区域。

## 注意事项

- 该命令执行后立即生效。

- 执行此命令删除配置前，执行RMV APNAREABNDN2TAI删除对应服务区域下的TAI范围配置，执行RMV MULDNNBINDAREA删除专网DNN绑定对应服务区域的配置。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AREANAME | APN相关服务区域 | 可选必选说明：必选参数<br>参数含义：该参数用于配置APN相关服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@APNAREA]] · APN相关服务区域（APNAREA）

## 使用实例

删除5G类型的TAI服务区域：

```
RMV APNAREA: AREANAME="dnnarea1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-APNAREA.md`
