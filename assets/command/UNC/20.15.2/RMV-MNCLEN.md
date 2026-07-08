---
id: UNC@20.15.2@MMLCommand@RMV MNCLEN
type: MMLCommand
name: RMV MNCLEN（删除MNC长度信息）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MNCLEN
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- MNC长度
status: active
---

# RMV MNCLEN（删除MNC长度信息）

## 功能

**适用NF：SMF**

该命令用于删除指定MCC号对应的MNC长度。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定移动国家码。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度是3。取值范围000～999。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MNCLEN]] · MNC长度信息（MNCLEN）

## 使用实例

删除当前UNC所属的MCC为460：

```
RMV MNCLEN:MCC="460";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除MNC长度信息（RMV-MNCLEN）_09652299.md`
