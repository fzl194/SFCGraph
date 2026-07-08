---
id: UNC@20.15.2@MMLCommand@ADD LACGROUP
type: MMLCommand
name: ADD LACGROUP（增加LAC组）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: LACGROUP
command_category: 配置类
applicable_nf:
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- 虚拟APN映射管理
- 基于LAC位置的虚拟APN映射管理
- 虚拟APN映射的LAC组
status: active
---

# ADD LACGROUP（增加LAC组）

## 功能

**适用NF：GGSN**

该命令用来添加LAC组。当需要在指定LAC组内绑定某个LAC号段时，使用该命令添加LAC组。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入3000条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LACGROUPNAME | LAC组名 | 可选必选说明：必选参数<br>参数含义：该参数用于指定TAC组名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~32。不支持空格，不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LACGROUP]] · LAC组（LACGROUP）

## 使用实例

假设运营商需要去添加一个新的LAC组名为“beijing”的LAC组，用于绑定LAC号段的绑定：

```
ADD LACGROUP:LACGROUPNAME="beijing";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加LAC组（ADD-LACGROUP）_09654412.md`
