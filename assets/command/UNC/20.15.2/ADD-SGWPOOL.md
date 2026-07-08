---
id: UNC@20.15.2@MMLCommand@ADD SGWPOOL
type: MMLCommand
name: ADD SGWPOOL（增加SGW POOL）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD SGWPOOL（增加SGW POOL）

## 功能

**适用NF：PGW-C**

该命令用于添加一个新的SGW POOL。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入20条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SGWPOOLNAME | SGW POOL名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定SGW POOL名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SGWPOOL]] · SGW POOL（SGWPOOL）

## 使用实例

假设用户需要添加一个名为“sgwpool1”的SGW POOL：

```
ADD SGWPOOL:SGWPOOLNAME="sgwpool1";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-SGWPOOL.md`
