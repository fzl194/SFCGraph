---
id: UNC@20.15.2@MMLCommand@RMV HSSBPOFC
type: MMLCommand
name: RMV HSSBPOFC（删除故障状态HSS）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: HSSBPOFC
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- 可靠性管理
- HSS故障BYPASS功能
status: active
---

# RMV HSSBPOFC（删除故障状态HSS）

## 功能

**适用网元：MME**

该命令用于删除故障状态HSS配置。

## 注意事项

- 该命令执行后立即生效。
- 删除局向HSS Bypass配置时，用户在后续业务流程恢复与HSS的交互，请确保主备HSS局向同时删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOSTNAME | 对端主机名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定进入故障状态的HSS主机名。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~127<br>默认值：无<br>配置原则：该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成或者配置为通配符（*）。该参数不区分大小写。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HSSBPOFC]] · 故障状态HSS（HSSBPOFC）

## 使用实例

删除对端主机名为"huawei"的故障状态HSS。

```
RMV HSSBPOFC: HOSTNAME="huawei";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-HSSBPOFC.md`
