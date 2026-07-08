---
id: UNC@20.15.2@MMLCommand@LST SMFALLOWEDARPS
type: MMLCommand
name: LST SMFALLOWEDARPS（查询5G用户允许的ARP列表）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFALLOWEDARPS
command_category: 查询类
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

# LST SMFALLOWEDARPS（查询5G用户允许的ARP列表）

## 功能

**适用NF：SMF**

该命令用于查询5G用户允许的ARP列表。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSINDEX | 用户QOS索引 | 可选必选说明：可选参数<br>参数含义：该参数表示允许用户接入的ARP列表索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFALLOWEDARPS]] · 5G用户允许的ARP列表（SMFALLOWEDARPS）

## 使用实例

如果想查询所有的5G用户允许的ARP列表，执行如下命令:

```
%%LST SMFALLOWEDARPS:;%%
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
          QOSINDEX  =  2
ARP Priority Level  =  ARP Priority Level 1&ARP Priority Level 2&ARP Priority Level 3&ARP Priority Level 4&ARP Priority Level 5&ARP Priority Level 6&ARP Priority Level 7&ARP Priority Level 8&ARP Priority Level 9&ARP Priority Level 10&ARP Priority Level 11&ARP Priority Level 12&ARP Priority Level 13&ARP Priority Level 14&ARP Priority Level 15
ARP Priority Level  =  NULL
           ARP PVI  =  NULL
(Number of results = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询5G用户允许的ARP列表（LST-SMFALLOWEDARPS）_13960448.md`
