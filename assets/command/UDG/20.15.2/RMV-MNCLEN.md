---
id: UDG@20.15.2@MMLCommand@RMV MNCLEN
type: MMLCommand
name: RMV MNCLEN（删除MNC长度信息）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: MNCLEN
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 路径管理
- PFCP路径管理
- UP信息管理
- MNC长度
status: active
---

# RMV MNCLEN（删除MNC长度信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于删除指定MCC号对应的MNC长度。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，为3位数字，000～999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [MNC长度信息（MNCLEN）](configobject/UDG/20.15.2/MNCLEN.md)

## 使用实例

删除当前UPF所属的MCC为460，MNC长度为2：

```
RMV MNCLEN:MCC="460";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除MNC长度信息（RMV-MNCLEN）_44865463.md`
