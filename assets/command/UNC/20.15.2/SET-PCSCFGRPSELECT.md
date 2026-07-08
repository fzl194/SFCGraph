---
id: UNC@20.15.2@MMLCommand@SET PCSCFGRPSELECT
type: MMLCommand
name: SET PCSCFGRPSELECT（设置P-CSCF组选择模式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PCSCFGRPSELECT
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- IMS管理
- P-CSCF管理
- P-CSCF组选择模式
status: active
---

# SET PCSCFGRPSELECT（设置P-CSCF组选择模式）

## 功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于配置apn或全局绑定的两个p-cscf-group的选择模式。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SELECTMODE |
| --- |
| MASTER_SLAVE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SELECTMODE | 选择模式 | 可选必选说明：可选参数<br>参数含义：该参数用于配置apn或全局绑定的两个p-cscf-group的选择模式。<br>数据来源：本端规划<br>取值范围：<br>- “MASTER_SLAVE（主备）”：表示绑定的两个p-cscf-group是主备方式。<br>- “LOAD_SHARING（负荷分担）”：表示绑定的两个p-cscf-group是负荷分担模式。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PCSCFGRPSELECT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PCSCFGRPSELECT]] · P-CSCF组选择模式（PCSCFGRPSELECT）

## 使用实例

当绑定的P-CSCF-GROUP是按负荷分担方式工作时，配置P-CSCF-GROUP按负荷分担方式选P-CSCF-GROUP：

```
SET PCSCFGRPSELECT:SELECTMODE=LOAD_SHARING;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置P-CSCF组选择模式（SET-PCSCFGRPSELECT）_09651601.md`
