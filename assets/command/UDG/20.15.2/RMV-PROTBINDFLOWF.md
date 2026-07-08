---
id: UDG@20.15.2@MMLCommand@RMV PROTBINDFLOWF
type: MMLCommand
name: RMV PROTBINDFLOWF（删除流过滤器协议绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PROTBINDFLOWF
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: ''
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 流过滤器的协议绑定
status: active
---

# RMV PROTBINDFLOWF（删除流过滤器协议绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除流过滤器协议绑定关系（RMV PROTBINDFLOWF）_82837372.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，可能会影响业务。

该命令用于删除协议与流过滤器绑定关系。

## 注意事项

- 该命令执行后60s生效。
- 如果不输入ProtocolName，则代表删除该FlowFilterName对应的流过滤器下所有的协议与流过滤器绑定关系。
- 该命令会导致用户匹配范围发生变化，可能导致性能下降。执行命令前请评估对性能的影响，如果无法评估请联系华为技术支持。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| PROTOCOLNAME | 协议名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [流过滤器协议绑定关系（PROTBINDFLOWF）](configobject/UDG/20.15.2/PROTBINDFLOWF.md)

## 使用实例

删除协议与流过滤器绑定关系：“FLOWFILTERNAME”为“testflowfiltername”, “PROTOCOLNAME”为“http”：

```
RMV PROTBINDFLOWF:FLOWFILTERNAME="testflowfiltername",PROTOCOLNAME="http";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流过滤器协议绑定关系（RMV-PROTBINDFLOWF）_82837372.md`
