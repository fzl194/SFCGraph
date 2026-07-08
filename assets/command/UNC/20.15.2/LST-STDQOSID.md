---
id: UNC@20.15.2@MMLCommand@LST STDQOSID
type: MMLCommand
name: LST STDQOSID（查询标准QoS ID配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STDQOSID
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- GGSN
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 标准QoS ID配置
status: active
---

# LST STDQOSID（查询标准QoS ID配置）

## 功能

**适用NF：SGW-C、PGW-C、GGSN、SMF**

该命令用于查询标准QoS ID配置。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSIDTYPE | QoS ID类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定QoS ID类型。<br>数据来源：本端规划<br>取值范围：<br>- “QCI（QCI）”：QCI<br>- “FIVEQI（5QI）”：5QI<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [标准QoS ID配置（STDQOSID）](configobject/UNC/20.15.2/STDQOSID.md)

## 使用实例

查询当前“标准QoS ID”配置：

```
%%LST STDQOSID:;%%
RETCODE = 0  操作成功

结果如下
--------
QoS ID类型  QoS ID起始值  QoS ID结束值  标准QoS ID的资源类型

QCI         65            67            指定QoS ID的资源类型为GBR
QCI         69            70            指定QoS ID的资源类型为Non-GBR
QCI         71            76            指定QoS ID的资源类型为GBR
QCI         79            80            指定QoS ID的资源类型为Non-GBR
5QI         65            67            指定QoS ID的资源类型为GBR
5QI         69            70            指定QoS ID的资源类型为Non-GBR
5QI         71            76            指定QoS ID的资源类型为GBR
5QI         79            80            指定QoS ID的资源类型为Non-GBR
5QI         82            86            指定QoS ID的资源类型为GBR
(结果个数 = 9)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询标准QoS-ID配置（LST-STDQOSID）_06399918.md`
