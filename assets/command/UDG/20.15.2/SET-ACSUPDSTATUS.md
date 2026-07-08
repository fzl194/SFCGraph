---
id: UDG@20.15.2@MMLCommand@SET ACSUPDSTATUS
type: MMLCommand
name: SET ACSUPDSTATUS（设置升级状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: ACSUPDSTATUS
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# SET ACSUPDSTATUS（设置升级状态）

## 功能

![](设置升级状态（SET ACSUPDSTATUS）_34280051.assets/notice_3.0-zh-cn.png)

该命令属于高危命令，执行该命令会设置升级状态，某些服务的状态会受到影响。若错误设置某些服务的升级状态，可能会导致该服务升级失败。请谨慎使用。

该命令用于设置RU升级开始和结束。

本命令只适用于ACS服务，其他微服务请使用SET UPDSTATUS命令。

## 注意事项

- 该命令执行后立即生效。
- 如果主主控没有设置升级开始，其他单板不能设置升级开始。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示资源单元名称。<br>数据来源：本端规划<br>取值范围：1-63位字符串，区分大小写，不支持空格。<br>默认值：无 |
| SETSTATUS | 设置状态 | 可选必选说明：必选参数<br>参数含义：该参数用于设置升级状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- On：开始升级。<br>- Off：结束升级。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/ACSUPDSTATUS]] · 升级状态（ACSUPDSTATUS）

## 使用实例

设置RU升级状态：

```
SET ACSUPDSTATUS:SETSTATUS=On;
SET ACSUPDSTATUS:SETSTATUS=Off;
SET ACSUPDSTATUS:RUNAME="VNODE_UGW_VNFC_OMU_0001",SETSTATUS=On;
SET ACSUPDSTATUS:RUNAME="VNODE_UGW_VNFC_SPU_0065",SETSTATUS=Off;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-ACSUPDSTATUS.md`
