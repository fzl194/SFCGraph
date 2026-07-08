---
id: UNC@20.15.2@MMLCommand@SET UPCALMRSTVAL
type: MMLCommand
name: SET UPCALMRSTVAL（设置UPC DS粒度N4请求等待超时异常的告警恢复阈值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: UPCALMRSTVAL
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UPC链路告警
status: active
---

# SET UPCALMRSTVAL（设置UPC DS粒度N4请求等待超时异常的告警恢复阈值）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于设置UPC DS粒度N4请求等待超时异常的告警恢复阈值。

## 注意事项

- 该命令执行后立即生效。

- 当前版本不支持此命令。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| UPCALMRSTVAL |
| --- |
| 60 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPCALMRSTVAL | UPC告警恢复阈值(秒) | 可选必选说明：可选参数<br>参数含义：UPC DS粒度N4请求等待超时异常的恢复告警阈值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是1~4294967295。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST UPCALMRSTVAL查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [UPC DS粒度N4请求等待超时异常的告警恢复阈值（UPCALMRSTVAL）](configobject/UNC/20.15.2/UPCALMRSTVAL.md)

## 使用实例

设置UPC DSDS粒度N4请求等待超时异常的告警恢复阈值为10秒：

```
SET UPCALMRSTVAL:UPCALMRSTVAL=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置UPC-DS粒度N4请求等待超时异常的告警恢复阈值（SET-UPCALMRSTVAL）_12701674.md`
