---
id: UDG@20.15.2@MMLCommand@SET GLBSMFATTR
type: MMLCommand
name: SET GLBSMFATTR（设置全局SMF属性）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: GLBSMFATTR
command_category: 配置类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- 业务控制策略
- 业务控制公共配置
- 对端SMF属性
status: active
---

# SET GLBSMFATTR（设置全局SMF属性）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

![](设置全局SMF属性（SET GLBSMFATTR）_44389967.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务

该命令用于设置UPF对接SMF是否为同一供应商提供的设备。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISSAMEPRV | SMF是否为同一供应商 | 可选必选说明：必选参数<br>参数含义：该参数用于设置UPF对接的SMF设备是否为同一供应商提供的设备。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- FALSE：与UPF对接的SMF设备是异厂商设备。<br>- TRUE：与UPF对接的SMF设备是同厂商设备。<br>默认值：无<br>配置原则：当UPF对接的SMF为非华为提供的设备时设置为FALSE。 |
| DEASSESSION | UPF去活会话 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISSAMEPRV”配置为“FALSE”时为必选参数。<br>参数含义：该参数用于设置UPF是否支持主动去活会话。<br>数据来源：全网规划<br>取值范围：枚举类型。<br>- DISABLE：不主动去活会话。<br>- ENABLE：主动去活会话。<br>默认值：无<br>配置原则：无 |
| CHGCONFLICTTM | N4计费上报消息冲突检查时长 | 可选必选说明：条件可选参数<br>前提条件：该参数在“ISSAMEPRV”配置为“TRUE”时为可选参数。<br>参数含义：该参数用于设置UPF收到会话去活请求时，检查N4计费上报消息冲突时长。当参数配置为零时，不做消息冲突检查；当配置为非零时，检查配置时长内是否存在N4计费上报请求消息未收响应，并在去活响应中通知SMF。<br>数据来源：对端协商<br>取值范围：0~5，单位：秒。<br>默认值：0<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/GLBSMFATTR]] · 全局SMF属性（GLBSMFATTR）

## 使用实例

设置为非同厂商SMF设备对接，支持主动去活会话：

```
SET GLBSMFATTR: ISSAMEPRV=FALSE, DEASSESSION = ENABLE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-GLBSMFATTR.md`
