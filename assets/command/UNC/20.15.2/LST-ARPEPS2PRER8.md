---
id: UNC@20.15.2@MMLCommand@LST ARPEPS2PRER8
type: MMLCommand
name: LST ARPEPS2PRER8（查询EPS ARP到Pre-R8 ARP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ARPEPS2PRER8
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- EPS ARP到PreR8 ARP映射
status: active
---

# LST ARPEPS2PRER8（查询EPS ARP到Pre-R8 ARP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于查询Gn接口和Gx接口之间ARP的映射值。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/ARPEPS2PRER8]] · EPS ARP到Pre-R8 ARP的映射规则（ARPEPS2PRER8）

## 使用实例

查询Gn接口和Gx接口之间ARP的映射值：

```
%%LST ARPEPS2PRER8:;%%
RETCODE = 0  操作成功

ARP的映射值配置信息
-------------------
ARP高优先级上限  =  5
ARP中优先级上限  =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-ARPEPS2PRER8.md`
