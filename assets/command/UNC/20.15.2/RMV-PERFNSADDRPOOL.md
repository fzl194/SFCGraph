---
id: UNC@20.15.2@MMLCommand@RMV PERFNSADDRPOOL
type: MMLCommand
name: RMV PERFNSADDRPOOL（删除切片地址池性能统计对象）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: PERFNSADDRPOOL
command_category: 配置类
applicable_nf:
- SMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# RMV PERFNSADDRPOOL（删除切片地址池性能统计对象）

## 功能

**适用NF：SMF**

该命令用于删除切片地址池性能统计对象。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IDX | 索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定切片地址池性能统计对象的索引。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~499。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PERFNSADDRPOOL]] · 切片地址池性能统计对象（PERFNSADDRPOOL）

## 使用实例

删除索引为1的性能统计对象：

```
RMV PERFNSADDRPOOL: IDX=1;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-PERFNSADDRPOOL.md`
