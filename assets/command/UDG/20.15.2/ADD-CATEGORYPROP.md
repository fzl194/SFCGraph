---
id: UDG@20.15.2@MMLCommand@ADD CATEGORYPROP
type: MMLCommand
name: ADD CATEGORYPROP（增加分类属性）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: CATEGORYPROP
command_category: 配置类
applicable_nf:
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
max_records: 500
category_path:
- 用户面服务管理
- 业务控制策略
- 带宽控制
- 分类属性
status: active
---

# ADD CATEGORYPROP（增加分类属性）

## 功能

**适用NF：PGW-U、UPF**

该命令用于配置带宽控制属性，用户进行带宽控制时，通过CATEPROPNAME匹配到相应的带宽控制策略，以完成带宽控制功能，用于关联预定义规则中的过滤条件进行ADC检测上报。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为500。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CATEPROPNAME | 分类属性名称 | 可选必选说明：必选参数<br>参数含义：该参数用于设置分类属性名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |
| CFGDOMAINNAME | 配置域名称 | 可选必选说明：可选参数<br>参数含义：该参数表示命令所属公共配置域的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/CATEGORYPROP]] · 分类属性（CATEGORYPROP）

## 关联任务

- [[UDG@20.15.2@Task@0-00032]]

## 使用实例

配置带宽控制属性：CATEPROPNAME为test：

```
ADD CATEGORYPROP:CATEPROPNAME="test";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/ADD-CATEGORYPROP.md`
