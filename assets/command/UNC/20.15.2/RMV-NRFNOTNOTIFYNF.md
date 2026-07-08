---
id: UNC@20.15.2@MMLCommand@RMV NRFNOTNOTIFYNF
type: MMLCommand
name: RMV NRFNOTNOTIFYNF（删除不通知NF实例）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFNOTNOTIFYNF
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF通知管理
status: active
---

# RMV NRFNOTNOTIFYNF（删除不通知NF实例）

## 功能

**适用NF：NRF**

该命令用于删除不通知的NF实例。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCEID | NF实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NF实例标识。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。<br>默认值：无<br>配置原则：<br>该命令与SET NRFNOTIFYPLY配合使用，当SET NRFNOTIFYPLY中的NOTIFYNPLY参数设置为“NFINSTANCEIDNOT”时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFNOTNOTIFYNF]] · 不通知NF实例（NRFNOTNOTIFYNF）

## 使用实例

若实例ID为"88888888-4444-1234-5678-123456789abc"的NF已经添加到了不通知列表中，现需要恢复NRF对该NF变更所触发的通知，执行如下命令。

```
RMV NRFNOTNOTIFYNF: NFINSTANCEID="88888888-4444-1234-5678-123456789abc";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除不通知NF实例（RMV-NRFNOTNOTIFYNF）_60089497.md`
