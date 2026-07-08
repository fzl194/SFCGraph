---
id: UNC@20.15.2@MMLCommand@ADD OCSGROUP
type: MMLCommand
name: ADD OCSGROUP（增加Ocs组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: OCSGROUP
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 100
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 在线计费
- OCS Diameter连接
- OCS Group
status: active
---

# ADD OCSGROUP（增加Ocs组）

## 功能

**适用NF：PGW-C、SMF**

此命令用来增加ocs组，配置ocs组的组名信息。

此命令为在线计费的基本配置，ocs组用来绑定OcsInfo。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 如果要使用该ocs组则必须绑定到dcc模板下。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| OCSGRPNAME | Ocs组名称 | 可选必选说明：必选参数<br>参数含义：ocs组的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OCSGROUP]] · Ocs组（OCSGROUP）

## 使用实例

增加一条Ocs组名称为“OcsGroup1”的配置，其中“OcsGrpName”为“OcsGroup1”：

```
ADD OCSGROUP:OCSGRPNAME="OcsGroup1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-OCSGROUP.md`
