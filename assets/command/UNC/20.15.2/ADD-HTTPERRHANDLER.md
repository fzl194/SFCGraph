---
id: UNC@20.15.2@MMLCommand@ADD HTTPERRHANDLER
type: MMLCommand
name: ADD HTTPERRHANDLER（增加间接路由代理故障重选配置）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: HTTPERRHANDLER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 可靠性管理
- 间接路由代理故障处理
status: active
---

# ADD HTTPERRHANDLER（增加间接路由代理故障重选配置）

## 功能

**适用NF：SMF**

该命令用于增加间接路由代理故障重选配置。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 对端网络功能类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定对端网元类型。<br>数据来源：本端规划<br>取值范围：<br>- “SMF（SMF）”：表示对端网元为SMF。<br>- “UDM（UDM）”：表示对端网元是UDM。<br>- “AMF（AMF）”：表示对端网元是AMF。<br>默认值：无<br>配置原则：无 |
| STATUSCODE | 状态码 | 可选必选说明：必选参数<br>参数含义：该参数用于指定状态码。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~1000。<br>默认值：无<br>配置原则：无 |
| RESENDSWITCH | 间接路由代理故障处理开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制开启和关闭间接路由代理故障处理功能。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：ENABLE<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/HTTPERRHANDLER]] · 间接路由代理故障重选配置（HTTPERRHANDLER）

## 使用实例

增加对端为UDM网络功能，状态码504的间接路由代理故障重选功能。

```
ADD HTTPERRHANDLER:NFTYPE=UDM,STATUSCODE=504,RESENDSWITCH=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-HTTPERRHANDLER.md`
