---
id: UNC@20.15.2@MMLCommand@RMV SGWCID
type: MMLCommand
name: RMV SGWCID（删除SGW-C网络标识符）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWCID
command_category: 配置类
applicable_nf:
- SGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- SGW-C信息管理
status: active
---

# RMV SGWCID（删除SGW-C网络标识符）

## 功能

**适用NF：SGW-C**

该命令用于删除SGW-C的全球唯一标识。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成SGW-C的全球唯一标识的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定组成SGW-C的全球唯一标识的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。只允许输入十进制数字（0-9）。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SGW-C网络标识符（SGWCID）](configobject/UNC/20.15.2/SGWCID.md)

## 使用实例

当运营商增加了SGW-C的全球唯一标识为123-45-00101，需要删除该标识时，执行命令如下：

```
RMV SGWCID:MCC="123",MNC="45";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除SGW-C网络标识符（RMV-SGWCID）_89867032.md`
