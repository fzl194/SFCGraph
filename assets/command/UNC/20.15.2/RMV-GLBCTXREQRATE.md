---
id: UNC@20.15.2@MMLCommand@RMV GLBCTXREQRATE
type: MMLCommand
name: RMV GLBCTXREQRATE（删除全局初始请求计费绑定关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: GLBCTXREQRATE
command_category: 配置类
applicable_nf:
- PGW-C
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 全局初始请求计费信息
status: active
---

# RMV GLBCTXREQRATE（删除全局初始请求计费绑定关系）

## 功能

**适用NF：PGW-C、SMF**

该命令用来删除全局的所有或者根据指定名字删除初始请求URR组的计费属性。

## 注意事项

- 该命令执行后立即生效。
- 当前版本不支持此命令。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTXRURRGRPNAME | 初始请求URR组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置计费属性名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GLBCTXREQRATE]] · 全局初始请求计费绑定关系（GLBCTXREQRATE）

## 使用实例

删除ChgProName为“urrgrp1”的全局初始请求URR组计费属性：

```
RMV GLBCTXREQRATE: CTXRURRGRPNAME="urrgrp1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除全局初始请求计费绑定关系（RMV-GLBCTXREQRATE）_09897184.md`
