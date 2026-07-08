---
id: UNC@20.15.2@MMLCommand@RMV EXTENDQCIMAP
type: MMLCommand
name: RMV EXTENDQCIMAP（删除扩展QCI和标准QCI的映射关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: EXTENDQCIMAP
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 扩展QCI功能
- 扩展QCI和标准QCI映射
status: active
---

# RMV EXTENDQCIMAP（删除扩展QCI和标准QCI的映射关系）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除扩展QCI和标准QCI的映射关系。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTENDQCI | 扩展QCI的值 | 可选必选说明：必选参数<br>参数含义：该参数用来指定扩展QCI。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是10~255。<br>默认值：无<br>配置原则：<br>该参数值不能与命令ADD STDQOSID中配置的QoS ID一致。 |

## 操作的配置对象

- [扩展QCI和标准QCI的映射关系（EXTENDQCIMAP）](configobject/UNC/20.15.2/EXTENDQCIMAP.md)

## 使用实例

运营商需要删除当前“扩展QCI”和“标准QCI”的映射关系时需要该命令解除映射关系。删除“扩展QCI”为“133”的“扩展QCI”和“标准QCI”的映射关系：

```
RMV EXTENDQCIMAP:EXTENDQCI=133;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除扩展QCI和标准QCI的映射关系（RMV-EXTENDQCIMAP）_09652170.md`
