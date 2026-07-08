---
id: UDG@20.15.2@MMLCommand@RMV DNAI
type: MMLCommand
name: RMV DNAI（删除DNAI配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: DNAI
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- DN管理
- DNAI管理
- 数据网络接入标识
status: active
---

# RMV DNAI（删除DNAI配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除DNAI配置（RMV DNAI）_53878564.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，DNAI实例下有用户存在时不允许删除该DNAI实例。

该命令用来删除DNAI实例。

## 注意事项

- 该命令执行后立即生效。
- 执行RMV DNAI命令时，参数DNAI为必选参数。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNAI | 数据网络接入标识 | 可选必选说明：必选参数<br>参数含义：数据网络接入标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。名称中不能包含空格，不区分大小写。<br>默认值：无<br>配置原则：输入的DNAI名称需要符合DNAI命名规则。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/DNAI]] · DNAI配置（DNAI）

## 使用实例

删除名为"Huawei.com"的DNAI实例：

```
RMV DNAI:DNAI="Huawei.com";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-DNAI.md`
