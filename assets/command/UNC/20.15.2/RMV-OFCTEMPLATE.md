---
id: UNC@20.15.2@MMLCommand@RMV OFCTEMPLATE
type: MMLCommand
name: RMV OFCTEMPLATE（删除离线计费模板或者属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OFCTEMPLATE
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 离线计费
- 离线计费基础参数
- 离线计费模板
status: active
---

# RMV OFCTEMPLATE（删除离线计费模板或者属性）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用于删除离线计费模板或恢复参数的默认值。当指定ATTRIBUTE参数时，则恢复对应参数的默认值，当不指定ATTRIBUTE时，则删除离线计费模板。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OFCTEMPLATENAME | 离线计费模板名 | 可选必选说明：必选参数<br>参数含义：配置离线模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| ATTRIBUTE | 离线计费模板属性 | 可选必选说明：可选参数<br>参数含义：离线计费模板属性。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- THRESHOLD：表示恢复模板阈值的默认值。<br>- CDR_TRIGGER：表示恢复模板中的话单产生开关的默认值。<br>- CONTAINER_TRIGGER：表示恢复模板中的容器产生开关的默认值。<br>- TQM：表示恢复模板中的时长配额机制的默认值。<br>- CDR_VERSION：表示恢复模板中的话单版本的默认值。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OFCTEMPLATE]] · 离线计费模板（OFCTEMPLATE）

## 使用实例

删除一个名称为“ofc_test”的离线计费模板：

```
RMV OFCTEMPLATE:OFCTEMPLATENAME="ofc_test";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除离线计费模板或者属性（RMV-OFCTEMPLATE）_09896913.md`
