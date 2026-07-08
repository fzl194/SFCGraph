---
id: UNC@20.15.2@MMLCommand@RMV CDRFIELDTEMP
type: MMLCommand
name: RMV CDRFIELDTEMP（删除话单字段模板）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CDRFIELDTEMP
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
- 话单字段控制
- 话单字段模板
status: active
---

# RMV CDRFIELDTEMP（删除话单字段模板）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用来删除特定的话单字段模板。此命令用于在割接或者启动某些业务时删除话单字段模板的配置从而适应场景需求。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 话单字段模板名 | 可选必选说明：必选参数<br>参数含义：指定话单字段模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [话单字段模板（CDRFIELDTEMP）](configobject/UNC/20.15.2/CDRFIELDTEMP.md)

## 使用实例

删除名为“cdrfieldtemp”的话单字段模板，模板中定义的字段在话单中全部不再携带，用于客户的业务调整需要：

```
RMV CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除话单字段模板（RMV-CDRFIELDTEMP）_09896892.md`
