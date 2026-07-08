---
id: UNC@20.15.2@MMLCommand@RMV PGWHOSTNAME
type: MMLCommand
name: RMV PGWHOSTNAME（删除逻辑接口的PGW主机名）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PGWHOSTNAME
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- Diameter AAA管理
- P-GW Host Name配置
- P-GW逻辑接口主机名
status: active
---

# RMV PGWHOSTNAME（删除逻辑接口的PGW主机名）

## 功能

**适用NF：PGW-C**

此命令用于删除PGW-C逻辑接口主机名。根据网络规划，当需要修改逻辑接口主机名时，需要先执行该命令，再执行ADD PGWHOSTNAME命令。

## 注意事项

- 该命令执行后立即生效。

- 如果没有该配置，且配置需要向Diameter AAA上报hostname，可能导致Diameter AAA授权失败。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTFTYPE | 接口类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GTP-C接口类型。<br>数据来源：本端规划<br>取值范围：<br>- S5_P_OR_GN_OR_S2B（S5-P/Gn/S2b/S2a接口）<br>- S8_P_OR_GP_OR_S2B（S8-P/Gp/S2b/S2a接口）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [逻辑接口的PGW主机名（PGWHOSTNAME）](configobject/UNC/20.15.2/PGWHOSTNAME.md)

## 使用实例

根据网络规划，需要删除PGW-C接口类型为S5_P_OR_GN_OR_S2B的配置：

```
RMV PGWHOSTNAME: INTFTYPE=S5_P_OR_GN_OR_S2B;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除逻辑接口的PGW主机名（RMV-PGWHOSTNAME）_64343908.md`
