---
id: UNC@20.15.2@MMLCommand@RMV NSMAPPARABYPLMN
type: MMLCommand
name: RMV NSMAPPARABYPLMN（删除指定PLMN的网络切片映射参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NSMAPPARABYPLMN
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 网络切片映射管理
- 网络切片映射控制参数
status: active
---

# RMV NSMAPPARABYPLMN（删除指定PLMN的网络切片映射参数）

## 功能

**适用NF：AMF**

该命令用于删除指定PLMN用户的网络切片映射相关参数配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置用户归属PLMN的移动国家码信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。<br>默认值：无<br>配置原则：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于配置用户归属PLMN的移动网号信息。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是2~3。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NSMAPPARABYPLMN]] · 指定PLMN的网络切片映射参数（NSMAPPARABYPLMN）

## 使用实例

删除MCC为“123”、MNC为“45”的用户的网络切片映射相关参数策略，执行如下命令：

```
RMV NSMAPPARABYPLMN: MCC="123", MNC="45";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NSMAPPARABYPLMN.md`
