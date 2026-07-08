---
id: UNC@20.15.2@MMLCommand@RMV SMFALLOWEDARPS
type: MMLCommand
name: RMV SMFALLOWEDARPS（删除5G用户允许的ARP列表）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SMFALLOWEDARPS
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC允许接入的ARPs
status: active
---

# RMV SMFALLOWEDARPS（删除5G用户允许的ARP列表）

## 功能

**适用NF：SMF**

该命令用于删除5G用户允许的ARP列表。

## 注意事项

- 命令执行后只对新接入用户生效。

- 删除前请确认和"ISMFDFTQOSCTRL"命令及"SMFNONDFTQOSCTL"命令已不存在引用关系，否则不能删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSINDEX | 用户QOS索引 | 可选必选说明：必选参数<br>参数含义：该参数表示允许用户接入的ARP列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFALLOWEDARPS]] · 5G用户允许的ARP列表（SMFALLOWEDARPS）

## 使用实例

删除"允许用户接入的ARP列表索引"为1的5G用户允许的ARP列表，执行如下命令:

```
%%RMV SMFALLOWEDARPS: QOSINDEX=2;%%
RETCODE = 0  Operation succeeded

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除5G用户允许的ARP列表（RMV-SMFALLOWEDARPS）_58840355.md`
