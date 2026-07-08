---
id: UNC@20.15.2@MMLCommand@LST SCPFUNCSW
type: MMLCommand
name: LST SCPFUNCSW（查询间接路由功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SCPFUNCSW
command_category: 查询类
applicable_nf:
- AMF
- SMF
- SMSF
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 通信模式管理
- 间接路由管理
status: active
---

# LST SCPFUNCSW（查询间接路由功能）

## 功能

**适用NF：AMF、SMF、SMSF、NCG**

该命令用于显示间接路由功能和服务发现代理开关配置信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNFTYPE | 本端NF类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本端NF的类型。<br>数据来源：全网规划<br>取值范围：<br>- “AMF（AMF）”：NF类型为AMF<br>- “SMF（SMF）”：NF类型为SMF<br>- “SMSF（SMSF）”：NF类型为SMSF<br>- “CHF（CHF）”：NF类型为CHF<br>- “NWDAF（NWDAF）”：NF类型为NWDAF<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCPFUNCSW]] · 间接路由功能（SCPFUNCSW）

## 使用实例

运营商A需要查询间接路由功能配置。

```
%%LST SCPFUNCSW:;%%
RETCODE = 0  操作成功

结果如下
------------------------
本端NF类型  对端NF类型  间接路由功能开关  服务发现代理开关  区域位置开关  拨测开关

AMF         UDM         OFF               OFF               OFF           OFF
AMF         AUSF        OFF               OFF               OFF           OFF
AMF         PCF         OFF               OFF               OFF           OFF
AMF         AMF         OFF               OFF               OFF           OFF
AMF         SMF         OFF               OFF               OFF           OFF
AMF         SMSF        OFF               OFF               OFF           OFF
AMF         5G-EIR      OFF               OFF               OFF           OFF
SMF         UDM         OFF               OFF               OFF           OFF
SMF         PCF         OFF               OFF               OFF           OFF
SMF         CHF         OFF               OFF               OFF           OFF
SMF         AMF         OFF               OFF               OFF           OFF
SMF         SMF         OFF               OFF               OFF           OFF
SMSF        UDM         OFF               OFF               OFF           OFF
SMSF        AMF         OFF               OFF               OFF           OFF
CHF         CUSTOM_OCS  OFF               OFF               OFF           OFF
(结果个数 = 15)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SCPFUNCSW.md`
