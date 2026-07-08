---
id: UDG@20.15.2@MMLCommand@SET N6MBMODE
type: MMLCommand
name: SET N6MBMODE（配置N6mb接口数据传输的优选方式及端口范围）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: N6MBMODE
command_category: 配置类
applicable_nf:
- UPF
effect_mode: 立即生效
is_dangerous: true
max_records: 1
category_path:
- 用户面服务管理
- MBS管理
- N6mb接口模式配置
status: active
---

# SET N6MBMODE（配置N6mb接口数据传输的优选方式及端口范围）

## 功能

**适用NF：UPF**

![](配置N6mb接口数据传输的优选方式及端口范围（SET N6MBMODE）_44422306.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，端口范围与已有端口冲突时可能导致端到端业务不通。

该命令用于配置N6mb接口的数据传输的优选方式及端口范围。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 只支持配置最大3000个端口号。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识 | MODE | UDPSTARTPORT | UDPENDPORT |
| --- | --- | --- | --- |
| 初始值 | UNICAST | 1024 | 4023 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MODE | N6mb接口数据传输的优选方式 | 可选必选说明：必选参数<br>参数含义：配置N6mb接口优选的传输方式。<br>数据来源：对端协商<br>取值范围：枚举类型。<br>- UNICAST：N6mb接口优选单播传输方式。<br>默认值：无<br>配置原则：无 |
| UDPSTARTPORT | 起始的UDP端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“UNICAST”时为必选参数。<br>参数含义：起始的UDP端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |
| UDPENDPORT | 结束的UDP端口号 | 可选必选说明：条件必选参数<br>前提条件：该参数在“MODE”配置为“UNICAST”时为必选参数。<br>参数含义：结束的UDP端口号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1024～65535。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/N6MBMODE]] · N6mb接口数据传输的优选方式及端口配置（N6MBMODE）

## 使用实例

配置N6mb接口的数据传输优选方式为单播传输方式，起始端口号为1024，结束端口号为4023：

```
SET N6MBMODE: MODE=UNICAST, UDPSTARTPORT=1024, UDPENDPORT=4023;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-N6MBMODE.md`
