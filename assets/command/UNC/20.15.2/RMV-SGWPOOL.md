---
id: UNC@20.15.2@MMLCommand@RMV SGWPOOL
type: MMLCommand
name: RMV SGWPOOL（删除SGW POOL）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SGWPOOL
command_category: 配置类
applicable_nf:
- PGW-C
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 网络管理
- 业务快速恢复
- SGW Pool
status: active
---

# RMV SGWPOOL（删除SGW POOL）

## 功能

**适用NF：PGW-C**

该命令用于删除一个SGW POOL。假设该SGW POOL不需要再使用或者发生故障时，使用该命令。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWPOOL]] · SGW POOL（SGWPOOL）

## 使用实例

假设用户需要删除一个名为“sgwpool1”的SGW POOL：

```
RMV SGWPOOL:SGWPOOLNAME="sgwpool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SGWPOOL.md`
