---
id: UDG@20.15.2@MMLCommand@SET TOSOFTPARA
type: MMLCommand
name: SET TOSOFTPARA（设置TCP优化软参）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: TOSOFTPARA
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 对新流生效
is_dangerous: false
max_records: 1
category_path:
- TCP优化服务管理
- TCP软参
status: active
---

# SET TOSOFTPARA（设置TCP优化软参）

## 功能

**适用NF：UPF**

该命令用于设置TCP优化软参。

## 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SOFTPARA1 | TCP优化软参1 | 可选必选说明：可选参数<br>参数含义：设置TCP优化软参1。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：无 |
| SOFTPARA2 | TCP优化软参2 | 可选必选说明：可选参数<br>参数含义：设置TCP优化软参2。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：无 |
| SOFTPARA3 | TCP优化软参3 | 可选必选说明：可选参数<br>参数含义：设置TCP优化软参3。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/TOSOFTPARA]] · TCP优化软参（TOSOFTPARA）

## 使用实例

设置TCP优化软参：

```
SET TOSOFTPARA: SOFTPARA1=0, SOFTPARA2=0, SOFTPARA3=0;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-TOSOFTPARA.md`
