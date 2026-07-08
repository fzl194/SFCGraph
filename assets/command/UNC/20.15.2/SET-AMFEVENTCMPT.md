---
id: UNC@20.15.2@MMLCommand@SET AMFEVENTCMPT
type: MMLCommand
name: SET AMFEVENTCMPT（设置AMF事件订阅兼容性参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: AMFEVENTCMPT
command_category: 配置类
applicable_nf:
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 事件订阅接口管理
- AMF事件订阅兼容性参数管理
status: active
---

# SET AMFEVENTCMPT（设置AMF事件订阅兼容性参数）

## 功能

**适用NF：AMF**

该命令用于为AMF事件订阅通知消息设置兼容性控制参数。事件订阅为AMF与其它NF之间的服务化接口，通过本命令可以控制AMF是否在该接口的通知消息中携带指定的可选信元。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| GLOBALGNBID |
| --- |
| NO |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GLOBALGNBID | UE当前驻留的基站全局标识 | 可选必选说明：可选参数<br>参数含义：该参数用于控制上报事件订阅类型为LOCATION_REPORT、PRESENCE_IN_AOI_REPORT的通知消息时，是否携带UE当前驻留的基站全局标识。<br>数据来源：全网规划<br>取值范围：<br>- “YES（是）”：是<br>- “NO（否）”：否<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AMFEVENTCMPT]] · 事件订阅通知消息的兼容性控制参数（AMFEVENTCMPT）

## 使用实例

设置AMF事件订阅的兼容性参数"UE当前驻留的基站全局标识"为"YES"，执行如下命令。

```
%%SET AMFEVENTCMPT: GLOBALGNBID=YES;%%
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-AMFEVENTCMPT.md`
