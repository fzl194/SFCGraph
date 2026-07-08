---
id: UDG@20.15.2@MMLCommand@RMV APPPERFSTAT
type: MMLCommand
name: RMV APPPERFSTAT（删除应用性能统计）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: APPPERFSTAT
command_category: 配置类
applicable_nf:
- UPF
- PGW-U
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 媒体中继
- 应用性能统计
status: active
---

# RMV APPPERFSTAT（删除应用性能统计）

## 功能

**适用NF：UPF、PGW-U**

该命令用于删除一组应用性能统计。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPNAME | 应用名称 | 可选必选说明：必选参数<br>参数含义：该参数用来指定应用名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/APPPERFSTAT]] · 应用性能统计（APPPERFSTAT）

## 使用实例

该命令用于删除一组应用性能统计，则配置命令如下：

```
RMV APPPERFSTAT:APPNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除应用性能统计（RMV-APPPERFSTAT）_43992602.md`
