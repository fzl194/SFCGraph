---
id: UDG@20.15.2@MMLCommand@DSP RELAYDNSSTATUS
type: MMLCommand
name: DSP RELAYDNSSTATUS（显示媒体中继DNS服务器状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: RELAYDNSSTATUS
command_category: 查询类
applicable_nf:
- UPF
- PGW-U
effect_mode: ''
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 媒体中继DNS服务器状态
status: active
---

# DSP RELAYDNSSTATUS（显示媒体中继DNS服务器状态）

## 功能

**适用NF：UPF、PGW-U**

该命令用于显示媒体中继DNS服务器状态。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNSSERVERNAME | DNS服务器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定DNS服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 该参数使用ADD RELAYDNSSERVER命令配置生成。<br>- 该取值必须和ADD RELAYDNSSERVER中配置的“DNSSERVERNAME”参数取值相同。 |
| PODID | PodID | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的POD。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，区分大小写。<br>默认值：无<br>配置原则：无 |
| SERVICEID | ServiceID | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的ServiceID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~39。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/RELAYDNSSTATUS]] · 媒体中继DNS服务器状态（RELAYDNSSTATUS）

## 使用实例

显示媒体中继DNS服务器状态：

```
DSP RELAYDNSSTATUS: DNSSERVERNAME="test01";
```

```

RETCODE = 0  操作成功

结果如下
------------------------
DNS服务器名称    PodID        ServiceID  IPv4主DNS服务器状态            IPv4备DNS服务器状态           IPv6主DNS服务器状态            IPv6备DNS服务器状态

test01           relay-pod-0  7          Normal                         Normal                        None                           None
test01           relay-pod-0  6          Normal                         Normal                        None                           None
test01           relay-pod-0  1          Normal                         Normal                        None                           None
test01           relay-pod-0  5          Normal                         Normal                        None                           None
test01           relay-pod-0  0          Normal                         Normal                        None                           None
test01           relay-pod-0  2          Normal                         Normal                        None                           None
test01           relay-pod-0  3          Normal                         Normal                        None                           None
test01           relay-pod-0  4          Normal                         Normal                        None                           None
(结果个数 = 8)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-RELAYDNSSTATUS.md`
