---
id: UNC@20.15.2@MMLCommand@RMV E2ETRCEX
type: MMLCommand
name: RMV E2ETRCEX（删除端到端用户跟踪）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: E2ETRCEX
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 平台调测
- OM调测
status: active
---

# RMV E2ETRCEX（删除端到端用户跟踪）

## 功能

**适用网元：MME**

该命令用于删除指定的全网跟踪任务。

## 注意事项

请谨慎执行该命令，否则有可能导致网管和网元上的全网跟踪任务不一致。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TRCID | 跟踪ID | 可选必选说明：必选参数<br>参数含义：该参数用于表示全网跟踪任务的参考号。<br>数据来源：全网规划。<br>取值范围：0~65535<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/E2ETRCEX]] · 端到端用户跟踪（E2ETRCEX）

## 使用实例

删除TRCID为1的全网跟踪任务。

RMV E2ETRCEX: TRCID=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-E2ETRCEX.md`
