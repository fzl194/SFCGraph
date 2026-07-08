---
id: UNC@20.15.2@MMLCommand@RMV MSCCRCACT
type: MMLCommand
name: RMV MSCCRCACT（删除MSCC层异常返回码处理动作）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: MSCCRCACT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- 信用控制
- Mscc层返回码控制
status: active
---

# RMV MSCCRCACT（删除MSCC层异常返回码处理动作）

## 功能

**适用NF：PGW-C、SMF**

该命令用于删除MSCC层异常返回码的处理动作配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCCTMPLTNAME | 在线计费模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定在线计费模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |
| MSCCRC | MSCC层异常返回码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定MSCC层异常返回码。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～4。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MSCCRCACT]] · MSCC层异常返回码处理动作（MSCCRCACT）

## 使用实例

删除全局在线计费模板中MSCC异常返回码5012的处理动作：

```
RMV MSCCRCACT:DCCTMPLTNAME="global",MSCCRC="5012";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-MSCCRCACT.md`
