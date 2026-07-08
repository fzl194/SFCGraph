---
id: UDG@20.15.2@MMLCommand@SET SFEBFDPKTIPID
type: MMLCommand
name: SET SFEBFDPKTIPID（设置BFD报文IPID的使能标记）
nf: UDG
version: 20.15.2
verb: SET
object_keyword: SFEBFDPKTIPID
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 软转发报文调测
status: active
---

# SET SFEBFDPKTIPID（设置BFD报文IPID的使能标记）

## 功能

该命令用于控制BFD探测报文中IPID字段是否填充。IPID为IP报文头中Identification字段的简称，它为一个计数器，每发一个报文，IPID自增1，填充后可以方便查看报文流向，帮助问题定位。

## 注意事项

- 该命令执行后立即生效。
- 打开BFD探测报文中IPID的使能标记以后，会对转发性能有一定影响，建议在问题定位时使用。
- 设置命令后，有效期为2个小时。
- 该命令仅在IPv4协议场景下支持。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ENABLE | IPID字段填充使能标记 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BFD探测报文中的IPID字段是否被填充。值为TRUE表示开关打开，IPID会被填充，值为FALSE表示开关关闭，IPID为默认值0。<br>数据来源：本端规划<br>取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SFEBFDPKTIPID]] · BFD报文IPID的使能标记（SFEBFDPKTIPID）

## 使用实例

控制BFD探测报文中IPID字段是否填充：

```
SET SFEBFDPKTIPID: ENABLE = TRUE;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/SET-SFEBFDPKTIPID.md`
