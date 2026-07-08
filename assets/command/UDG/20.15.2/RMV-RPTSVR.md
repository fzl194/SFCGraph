---
id: UDG@20.15.2@MMLCommand@RMV RPTSVR
type: MMLCommand
name: RMV RPTSVR（删除报表服务器）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: RPTSVR
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务报表管理
- 报表服务器管理
- 报表服务器
status: active
---

# RMV RPTSVR（删除报表服务器）

## 功能

**适用NF：PGW-U、UPF**

该命令用于删除报表服务器。当希望删除报表服务器，则配置该命令。

## 注意事项

- 该命令执行后立即生效。
- 如果RptSvr被RptSvrAddr绑定，删除时，需要将绑定关系解除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RPTSVRNAME | 报表服务器名称 | 可选必选说明：必选参数<br>参数含义：设置报表服务器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [报表服务器（RPTSVR）](configobject/UDG/20.15.2/RPTSVR.md)

## 使用实例

删除报表服务器report01：

```
RMV RPTSVR: RPTSVRNAME="report01";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除报表服务器（RMV-RPTSVR）_79568180.md`
