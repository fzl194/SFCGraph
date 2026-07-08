---
id: UDG@20.15.2@MMLCommand@CLR INTERFACEPERF
type: MMLCommand
name: CLR INTERFACEPERF（清除逻辑口报文统计信息）
nf: UDG
version: 20.15.2
verb: CLR
object_keyword: INTERFACEPERF
command_category: 动作类
applicable_nf:
- SGW-U
- PGW-U
- UPF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 用户面服务管理
- DN管理
- 逻辑接口管理
- 逻辑接口统计
- 清除接口统计
status: active
---

# CLR INTERFACEPERF（清除逻辑口报文统计信息）

## 功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来清除接口输入输出报文的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| INTERFACENAME | 逻辑接口名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定要查询的逻辑接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@INTERFACEPERF]] · 逻辑口报文统计信息（INTERFACEPERF）

## 使用实例

当运营商需要统计一定时间内某接口的流量信息时，这时必须在统计开始前清除该接口原有的统计信息，使接口重新进行统计：

```
CLR INTERFACEPERF:INTERFACENAME="saif1/0/0";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/CLR-INTERFACEPERF.md`
