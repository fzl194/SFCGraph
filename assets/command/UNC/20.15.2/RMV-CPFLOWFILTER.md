---
id: UNC@20.15.2@MMLCommand@RMV CPFLOWFILTER
type: MMLCommand
name: RMV CPFLOWFILTER（删除CP流过滤器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CPFLOWFILTER
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- SGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- N4 GTP-U管理
- 流过滤器
status: active
---

# RMV CPFLOWFILTER（删除CP流过滤器）

## 功能

**适用NF：SMF、PGW-C、SGW-C、GGSN**

该命令用于删除SMF和UPF之间的消息流过滤器。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FLOWFILTERNAME | 流过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SMF和UPF之间的消息流过滤器名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [CP流过滤器（CPFLOWFILTER）](configobject/UNC/20.15.2/CPFLOWFILTER.md)

## 使用实例

删除SMF和UPF之间的IPv6 RS消息流过滤器：

```
RMV CPFLOWFILTER: FLOWFILTERNAME="RS";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除CP流过滤器（RMV-CPFLOWFILTER）_96805497.md`
