---
id: UDG@20.15.2@MMLCommand@RMV FLTBINDFLOWF
type: MMLCommand
name: RMV FLTBINDFLOWF（删除流过滤器的过滤器绑定关系）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: FLTBINDFLOWF
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
- 流过滤器的过滤器绑定
status: active
---

# RMV FLTBINDFLOWF（删除流过滤器的过滤器绑定关系）

## 功能

**适用NF：PGW-U、UPF**

![](删除流过滤器的过滤器绑定关系（RMV FLTBINDFLOWF）_82837367.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除FltBindFlowF可能会改变业务匹配结果，影响策略获取，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除过滤器与流过滤器绑定关系。

## 注意事项

- 该命令执行后60s生效。
- 如果不输入FilterName，则代表删除该FlowFilterName对应的流过滤器下所有的过滤器与流过滤器绑定关系。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置流过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| FILTERNAME | 过滤器名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/FLTBINDFLOWF]] · 流过滤器的过滤器绑定关系（FLTBINDFLOWF）

## 使用实例

删除过滤器与流过滤器绑定关系，FLOWFILTERNAME为“testflowfiltername”，FILTERNAME为“testfiltername”：

```
RMV FLTBINDFLOWF:FLOWFILTERNAME="testflowfiltername",FILTERNAME="testfiltername";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除流过滤器的过滤器绑定关系（RMV-FLTBINDFLOWF）_82837367.md`
