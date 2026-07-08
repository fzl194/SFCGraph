---
id: UDG@20.15.2@MMLCommand@ADD BGPCONFED
type: MMLCommand
name: ADD BGPCONFED（增加联盟中自治系统）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: BGPCONFED
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 32
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- BGP管理
- 联盟中自治系统
status: active
---

# ADD BGPCONFED（增加联盟中自治系统）

## 功能

该命令用于指定属于同一个联盟的各子自治系统号。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为32。
- 执行前先要设置BGP的联盟号。
- 该操作将导致联盟子自治域的邻居复位。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CONFEDASNUMBER | 联盟对等体的自治域号 | 可选必选说明：必选参数<br>参数含义：该参数用于指定与本地AS连接的其他EBGP对等体所属的子自治系统号。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围为1～11。取值范围是number<1-4294967295>或者number<1-65535>.number<0-65535>。<br>默认值：无 |

## 操作的配置对象

- [联盟中自治系统（BGPCONFED）](configobject/UDG/20.15.2/BGPCONFED.md)

## 使用实例

设置BGP的联盟号，将子系统AS号65002加入到联盟里：

```
SET BGP:BGPENABLE=TRUE,CONFEDIDNUMBER="230";
ADD BGPCONFED:CONFEDASNUMBER="65002";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/增加联盟中自治系统（ADD-BGPCONFED）_00840705.md`
