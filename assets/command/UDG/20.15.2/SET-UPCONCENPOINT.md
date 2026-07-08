---
id: UDG@20.15.2@MMLCommand@SET UPCONCENPOINT
type: MMLCommand
name: SET UPCONCENPOINT（设置集中点部署模式）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: UPCONCENPOINT
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- Diameter管理
- 集中点模式
status: active
---

# SET UPCONCENPOINT（设置集中点部署模式）

## 功能

**适用NF：UPF**

![](设置集中点部署模式（SET UPCONCENPOINT）_97314577.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，修改集中点模式可能导致Diameter链路重建或中断，进而影响用户使用业务，比如用户被去活等。涉及Diameter链路的接口为Swm接口。

此命令用于设置信令集中点的部署模式。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- LOCALIP_PEER模式下，ADD UPDIAMCONN命令添加的链路，仅LocalPort参数未配置或配置为0的链路生效。LocalPort参数配置为非0的链路，允许配置下发，但是不会建链。
- LOCALPORT模式下，ADD UPDIAMCONN命令添加的链路，仅LocalPort参数配置为非0的链路生效。LocalPort参数未配置或配置为0的链路，允许配置下发，但是不会建链。
- 如果Swm集中点模式在LOCALIP_PEER和LOCALPORT之间切换，需要使用命令RMV UPSCTPASSOC删除原模式下的SCTP耦联测量对象并重新配置。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | SWMCONCENMODE |
| --- | --- |
| 初始值 | LOCALIP_PEER |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWMCONCENMODE | Swm集中点模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指定Swm集中点的部署模式。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- LOCALIP_PEER：按照本端源IP加对端主机名绑定Diameter应用的集中点。<br>- LOCALPORT：按照本端端口绑定Diameter集中点。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@UPCONCENPOINT]] · 集中点部署模式（UPCONCENPOINT）

## 使用实例

根据网络规划，需要修改Swm集中点的部署模式为LOCALPORT，则可以按如下配置：

```
SET UPCONCENPOINT: SWMCONCENMODE=LOCALPORT;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-UPCONCENPOINT.md`
