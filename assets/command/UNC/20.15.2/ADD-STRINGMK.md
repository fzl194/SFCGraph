---
id: UNC@20.15.2@MMLCommand@ADD STRINGMK
type: MMLCommand
name: ADD STRINGMK（增加字符串类型Monitoring-Key）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: STRINGMK
command_category: 配置类
applicable_nf:
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费和策略的业务管理
- 业务策略
- 字符串Monitoring-Key
status: active
---

# ADD STRINGMK（增加字符串类型Monitoring-Key）

## 功能

**适用NF：PGW-C、GGSN**

该命令用于配置字符串类型的Monitoring-Key。

## 注意事项

- 该命令执行后立即生效。

- 如果Gx接口配置过数值类型的mk（LST URR），不允许新增stringMK。
- 配置stringmk后，Gx接口只能绑定字符类型的mk。

- 最多可输入256条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MKSTRVALUE | 字符串Monitoring-Key | 可选必选说明：必选参数<br>参数含义：该参数用于配置字符串类型的Monitoring-Key。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~31。不支持空字符串，但支持字符串中出现空格。区分大小写。<br>默认值：无<br>配置原则：无 |
| MKNUMVALUE | 监控属性值 | 可选必选说明：必选参数<br>参数含义：设置监控属性的ID。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~4294967294。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@STRINGMK]] · 字符串类型Monitoring-Key（STRINGMK）

## 使用实例

假如运营商需要配置一个字符型的MK，名字是“test”,值为100：

```
ADD STRINGMK: MKSTRVALUE="test", MKNUMVALUE=100;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-STRINGMK.md`
