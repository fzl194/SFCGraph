---
id: UNC@20.15.2@MMLCommand@RMV L2FILTER
type: MMLCommand
name: RMV L2FILTER（删除层二过滤器）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: L2FILTER
command_category: 配置类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务模板
- 层二过滤器
status: active
---

# RMV L2FILTER（删除层二过滤器）

## 功能

**适用NF：SMF**

该命令用于删除层二过滤器。

## 注意事项

- 该命令执行后只对新接入的会话生效。

- 如果存在引用了层二过滤器名称的层二规则记录，则不允许删除层二过滤器。层二规则记录通过LST L2RULE查询。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| FILTERNAME | 层二过滤器名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定层二过滤器名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [层二过滤器（L2FILTER）](configobject/UNC/20.15.2/L2FILTER.md)

## 使用实例

删除层二过滤器名称为“filter1”的层二过滤器：

```
RMV L2FILTER: FILTERNAME="filter1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除层二过滤器（RMV-L2FILTER）_23622994.md`
