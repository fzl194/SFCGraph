---
id: UNC@20.15.2@MMLCommand@ADD GLBCTXREQRATE
type: MMLCommand
name: ADD GLBCTXREQRATE（增加全局初始请求计费绑定关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: GLBCTXREQRATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
max_records: 10
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 全局初始请求计费信息
status: active
---

# ADD GLBCTXREQRATE（增加全局初始请求计费绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来配置全局的初始请求URR组名称的计费属性。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为10。
- 配置全局的初始请求URR组名称的计费属性前需要先配置URRGroup。
- 全局下最多可以配置10个计费属性。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTXRURRGRPNAME | 初始请求URR组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置计费属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCTXREQRATE]] · 全局初始请求计费绑定关系（GLBCTXREQRATE）

## 使用实例

配置全局的初始请求URR组名称的计费属性，对应的URRGroup为“urrgrp1”：

```
ADD GLBCTXREQRATE: CTXRURRGRPNAME="urrgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加全局初始请求计费绑定关系（ADD-GLBCTXREQRATE）_09897183.md`
