---
id: UDG@20.15.2@MMLCommand@SET TMMSGFC
type: MMLCommand
name: SET TMMSGFC（设置跟踪消息流控状态）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TMMSGFC
command_category: 配置类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 消息跟踪
status: active
---

# SET TMMSGFC（设置跟踪消息流控状态）

## 功能

该命令用于设置跟踪消息流控状态。

从跟踪服务到Web客户端的消息流控操作前后，均能够以每秒500条的消息推送。

> **说明**
> 由于跟踪能力提升，跟踪推送消息默认条数基线从100条增加到500条。

> **说明**
> - 该命令存在系统初始记录，参数“客户端启用流控”的初始设定值为“YES(是)”。
> - 当客户端启用流控设置为“NO(否)”时，会导致在线跟踪功能性能下降。

## 参数

| **参数标识** | **参数名称** | **参数说明** |
| --- | --- | --- |
| FLOWCONTROL | 客户端启用流控 | 可选必选说明：必选参数。<br>参数含义：用于指定从跟踪服务到Web客户端的消息是否开启流控。<br>取值范围：<br>- “YES(是)”：表示开启流控。<br>- “NO(否)”：表示关闭流控。<br>默认值：无。<br>配置原则：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TMMSGFC]] · 跟踪消息流控状态（TMMSGFC）

## 使用实例

设置跟踪消息流控状态：

```
%%SET TMMSGFC: FLOWCONTROL=YES;%%
RETCODE = 0  操作成功

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/设置跟踪消息流控状态（SET-TMMSGFC）_37693591.md`
