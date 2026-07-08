---
id: UDG@20.15.2@MMLCommand@RMV USRRELATEIDEN
type: MMLCommand
name: RMV USRRELATEIDEN（删除用户关联识别）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: USRRELATEIDEN
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
- 三四层规则管理
- 用户关联识别
status: active
---

# RMV USRRELATEIDEN（删除用户关联识别）

## 功能

**适用NF：PGW-U、UPF**

![](删除用户关联识别（RMV USRRELATEIDEN）_82837435.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除UsrRelateIden可能改变协议识别结果，影响策略获取。

当运营商业务变更，为了提高系统性能，删除用户关联识别功能时配置，该命令用于删除指定的用户关联识别配置，该命令支持批量删除。

## 注意事项

该命令执行后60s生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROTOCOLNAME | 协议名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置对应的协议名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：数据源为系统支持识别的所有类型的协议、子协议，可以通过工程命令smctrldsp protocol-list查询。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/USRRELATEIDEN]] · 用户关联识别（USRRELATEIDEN）

## 使用实例

假设运营商不需要对https协议提高识别率，删除指定的协议的用户关联识别功能配置：

```
RMV USRRELATEIDEN:  PROTOCOLNAME="https";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-USRRELATEIDEN.md`
