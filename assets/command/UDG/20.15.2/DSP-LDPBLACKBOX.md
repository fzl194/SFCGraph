---
id: UDG@20.15.2@MMLCommand@DSP LDPBLACKBOX
type: MMLCommand
name: DSP LDPBLACKBOX（显示LDP记录的黑匣子信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: LDPBLACKBOX
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- LDP维护
status: active
---

# DSP LDPBLACKBOX（显示LDP记录的黑匣子信息）

## 功能

该命令用于显示LDP记录的黑匣子信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| COMPTYPE | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示组件类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- NEIGH_MANAGER：邻居管理组件。<br>- SESS_MANAGER：会话管理组件。<br>- LSP_MANAGER：LSP管理组件。<br>默认值：无 |
| BLACKBOXTYPE | 黑匣子类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“COMPTYPE”配置为“NEIGH_MANAGER” 或 “SESS_MANAGER”时为必选参数。<br>参数含义：该参数用于表示黑匣子类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：本地信息。<br>- COMPONENT：指定组件的信息。<br>- SESSION：会话信息。<br>默认值：无 |
| LSPBLACKBOXTYPE | LDPM组件的黑匣子类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“COMPTYPE”配置为“LSP_MANAGER”时为必选参数。<br>参数含义：该参数用于表示LDPM组件的黑匣子类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCAL：本地信息。<br>- COMPONENT：指定组件的信息。<br>默认值：无 |
| COMPONENTID | 组件PID或CID | 可选必选说明：条件必选参数<br>前提条件：该参数在“BLACKBOXTYPE”配置为“COMPONENT”时为必选参数。<br>可选必选说明：条件必选参数<br>前提条件：该参数在“LSPBLACKBOXTYPE”配置为“COMPONENT”时为必选参数。<br>参数含义：该参数用于表示组件PID或CID。<br>数据来源：本端规划<br>取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。<br>默认值：无 |

## 操作的配置对象

- [LDP记录的黑匣子信息（LDPBLACKBOX）](configobject/UDG/20.15.2/LDPBLACKBOX.md)

## 使用实例

显示LDP的会话管理组件记录的本地信息：

```
DSP LDPBLACKBOX:COMPTYPE=SESS_MANAGER,BLACKBOXTYPE=COMPONENT,COMPONENTID="0x80810086";
```

```

RETCODE = 0  操作成功。

结果如下
--------
LDPM组件记录的黑匣子信息

[M] [11- 7  9:24:13]:[PDPWE3 Comp]Send msg to pwe3, OP: 0, SN: 1, Ret: 0

[M] [11- 7  9:25: 9]:[PDPWE3 Comp]Send msg to pwe3, OP: 6, SN: 2, Ret: 0

[M] [11- 7  9:25: 9]:[PDPWE3 Comp]LDC send PWE3 batch backup end ACK

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Send msg to pwe3, OP: 9, SN: -1, Ret: 0

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Receive pwe3 out msg bd req ack

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Receive pwe3 out msg bd end

[M] [11- 7  9:25:14]:[PDPWE3 Comp]Send msg to pwe3, OP: 10, SN: 3, Ret: 0
(结果个数 = 7)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示LDP记录的黑匣子信息（DSP-LDPBLACKBOX）_00441025.md`
