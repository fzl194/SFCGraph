---
id: UNC@20.15.2@MMLCommand@RMV OCSBINDING
type: MMLCommand
name: RMV OCSBINDING（删除Ocs绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: OCSBINDING
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
- OCS Diameter连接
- OCS绑定OCS Group
status: active
---

# RMV OCSBINDING（删除Ocs绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除OCS绑定关系。支持批量删除，给OCSGRPNAM字段赋值，删除指定OCSGRPNAM的记录；给OCSGRPNAME和OCSHOSTNAME字段赋值，删除满足条件的记录。

## 注意事项

- 该命令执行后立即生效。
- 当未指定Ocs主机名称时，禁止执行该命令。若需要执行，需将软参BYTE976的值设置为169。
- 删除OCS绑定关系后，对应新激活在线计费用户立即生效，可能导致该用户激活失败。
- 删除OCS绑定关系后，对应已经选择该OCS服务器的在线计费用户，如果链路正常的话，仍然会选择该OCS服务器发送消息。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：必选参数<br>参数含义：指定OCS组名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格。<br>默认值：无<br>配置原则：无 |
| OCSHOSTNAME | Ocs主机名称 | 可选必选说明：可选参数<br>参数含义：指定OCS主机名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～127。不支持空格。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSBINDING]] · Ocs绑定关系（OCSBINDING）

## 使用实例

删除OCS绑定关系，OCSGRPNAME为test，OCSHOSTNAME为test01，命令为：

```
RMV OCSBINDING:OCSGRPNAME="test",OCSHOSTNAME="test01";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除Ocs绑定关系（RMV-OCSBINDING）_09896965.md`
