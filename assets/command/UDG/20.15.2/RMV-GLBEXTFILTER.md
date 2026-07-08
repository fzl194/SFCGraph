---
id: UDG@20.15.2@MMLCommand@RMV GLBEXTFILTER
type: MMLCommand
name: RMV GLBEXTFILTER（删除全局扩展过滤器绑定配置）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GLBEXTFILTER
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: true
category_path:
- 用户面服务管理
- 业务匹配策略
- 业务过滤器管理
- 流过滤器管理
- 全局扩展过滤器绑定
status: active
---

# RMV GLBEXTFILTER（删除全局扩展过滤器绑定配置）

## 功能

**适用NF：PGW-U、UPF**

![](删除全局扩展过滤器绑定配置（RMV GLBEXTFILTER）_82837358.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，删除扩展过滤器会影响重定向动作的业务范围可能导致用户业务受损，请谨慎使用并联系华为支持协助操作。

该命令用于删除全局扩展过滤器绑定关系。如果只删除指定扩展过滤器，按照未删除其他过滤器绑定关系执行匹配动作，如果删除全部扩展过滤器，将会直接执行已经匹配成功的URL重定向（使用ADD REDIRECT或MOD REDIRECT配置）或智能重定向动作（在ADD RULE或MOD RULE配置时指定Policy Type为SMARTREDIRECT）。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| EXTFLTNAME | 扩展过滤器名字 | 可选必选说明：可选参数<br>参数含义：该参数用于指定扩展过滤器名字。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：<br>- 如果输入过滤器名称，表示删除指定的过滤器条件，删除后此参数取值恢复为初始值NULL。<br>- 如果不输入任何名称，表示删除全部条件。 |

## 操作的配置对象

- [全局扩展过滤器绑定配置（GLBEXTFILTER）](configobject/UDG/20.15.2/GLBEXTFILTER.md)

## 使用实例

删除扩展过滤名称为ExtFilter1的全局扩展过滤器绑定关系，使用此命令：

```
RMV GLBEXTFILTER:EXTFLTNAME="ExtFilter1";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除全局扩展过滤器绑定配置（RMV-GLBEXTFILTER）_82837358.md`
