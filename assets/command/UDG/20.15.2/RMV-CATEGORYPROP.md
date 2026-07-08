---
id: UDG@20.15.2@MMLCommand@RMV CATEGORYPROP
type: MMLCommand
name: RMV CATEGORYPROP（删除分类属性）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: CATEGORYPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 分类属性
status: active
---

# RMV CATEGORYPROP（删除分类属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用来删除所有或者根据分类属性名字删除配置信息。

## 注意事项

- 该命令执行后立即生效。
- 若CATEGORYPROP配置信息被BWMSERVICE绑定，则不允许删除。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CATEPROPNAME | 分类属性名称 | 可选必选说明：可选参数<br>参数含义：该参数用于设置分类属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CATEGORYPROP]] · 分类属性（CATEGORYPROP）

## 使用实例

删除名称为“test”的分类属性配置信息：

```
RMV CATEGORYPROP:CATEPROPNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除分类属性（RMV-CATEGORYPROP）_82837505.md`
