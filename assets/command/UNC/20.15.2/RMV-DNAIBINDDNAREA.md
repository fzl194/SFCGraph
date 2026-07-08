---
id: UNC@20.15.2@MMLCommand@RMV DNAIBINDDNAREA
type: MMLCommand
name: RMV DNAIBINDDNAREA（删除DNAI支持的服务区域）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DNAIBINDDNAREA
command_category: 配置类
applicable_nf:
- SGW-C
- SMF
- GGSN
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- DNAI位置绑定区域管理
status: active
---

# RMV DNAIBINDDNAREA（删除DNAI支持的服务区域）

## 功能

**适用NF：SGW-C、SMF、GGSN、PGW-C**

该命令用于删除DNAI支持的服务区域。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络访问标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定数据网络访问标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~63。不区分大小写。<br>默认值：无<br>配置原则：无 |
| AREANAME | DNAI服务区域名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNAI服务区域名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。不能为非法字符，只允许输入字母，数字、“_”、“.”，并且开头和结尾只能是数字或者字母，不能出现连续两个“.”。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNAIBINDDNAREA]] · DNAI支持的服务区域（DNAIBINDDNAREA）

## 使用实例

删除数据网络访问标识为“ulcl”绑定的服务区域“DNAREA1”。

```
RMV DNAIBINDDNAREA: DNAI="ulcl", AREANAME="dnarea1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-DNAIBINDDNAREA.md`
