---
id: UNC@20.15.2@MMLCommand@SET PFCPCMPT
type: MMLCommand
name: SET PFCPCMPT（设置PFCP接口兼容性参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: PFCPCMPT
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- PFCP接口兼容性
status: active
---

# SET PFCPCMPT（设置PFCP接口兼容性参数）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于设置PFCP接口兼容性参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| BAR | POOLPLACEHOLDER | NWINTVPN |
| --- | --- | --- |
| NOT_SUPPORT | FALSE | FALSE |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BAR | 是否支持BAR信元 | 可选必选说明：可选参数<br>参数含义：该参数用于控制PFCP接口是否支持BAR（Buffering Action Rule）信元。<br>数据来源：全网规划<br>取值范围：<br>- “SUPPORT（支持）”：支持BAR信元<br>- “NOT_SUPPORT（不支持）”：不支持BAR信元<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PFCPCMPT查询当前参数配置值。<br>配置原则：无 |
| POOLPLACEHOLDER | 是否携带地址池占位符 | 可选必选说明：可选参数<br>参数含义：该参数用于指定PFCP接口消息是否支持携带地址池占位符。UNC向UDG申请双栈地址的时候，如果只有IPv6类型的地址池，则将IPv4地址池的位置用*代替，即为占位符。<br>以免对端将IPv6类型的地址池识别成IPv4类型。<br>数据来源：对端协商<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PFCPCMPT查询当前参数配置值。<br>配置原则：无 |
| NWINTVPN | 路由实例是否填写VPN | 可选必选说明：可选参数<br>参数含义：该参数用于控制PFCP接口中N6口PDR的Network Instance信元是否填写VPN。<br>数据来源：全网规划<br>取值范围：<br>- TRUE(TRUE)<br>- FALSE(FALSE)<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PFCPCMPT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PFCPCMPT]] · PFCP接口兼容性参数（PFCPCMPT）

## 使用实例

设置PFCP接口兼容性，执行如下命令：

```
SET PFCPCMPT:BAR = NOT_SUPPORT,POOLPLACEHOLDER=FALSE;NWINTVPN=FALSE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-PFCPCMPT.md`
