---
id: UDG@20.15.2@MMLCommand@RMV GRETUNNEL
type: MMLCommand
name: RMV GRETUNNEL（删除GRE隧道）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: GRETUNNEL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- VPN管理
- GRE管理
- GRE隧道
status: active
---

# RMV GRETUNNEL（删除GRE隧道）

## 功能

该命令用于删除GRE隧道。

当网络重新规划，之前创建的GRE隧道不再使用。此时可执行该命令删除已创建的GRE隧道。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TNLNAME | 隧道名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定GRE隧道接口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：字符串形式为Tunnel+接口编号。 接口编号为一维或三维（格式为X/Y/Z）。 |
| TNLTYPE | 隧道类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定隧道类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- gre：指定隧道类型为Gre。<br>- gre6：指定隧道类型为Gre6。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@GRETUNNEL]] · GRE隧道（GRETUNNEL）

## 使用实例

已建立GRE隧道Tunnel1，现需要删除该隧道：

```
RMV GRETUNNEL:TNLNAME="Tunnel1",TNLTYPE=gre;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/RMV-GRETUNNEL.md`
