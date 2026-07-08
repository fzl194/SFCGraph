---
id: UNC@20.15.2@MMLCommand@SET LINKMTU
type: MMLCommand
name: SET LINKMTU（设置Link MTU值）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: LINKMTU
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 本局信息管理
- SMF
- LINKMTU
status: active
---

# SET LINKMTU（设置Link MTU值）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用来设置UNC在PCO信元中响应给终端的IPv4 Link MTU值和Non-IP Link MTU值。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MTUSW | IPV4LINKMTU | NONIPLINKMTU |
| --- | --- | --- |
| DISABLE | 1358 | 1358 |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MTUSW | 携带Link MTU开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制UNC是否在PCO信元中携带Link MTU值给终端。<br>数据来源：全网规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKMTU查询当前参数配置值。<br>配置原则：无 |
| IPV4LINKMTU | IPv4 Link MTU | 可选必选说明：该参数在"MTUSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置UNC在PCO信元中响应给终端的IPv4 Link MTU值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是128~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKMTU查询当前参数配置值。<br>配置原则：无 |
| NONIPLINKMTU | Non-IP Link MTU | 可选必选说明：该参数在"MTUSW"配置为"ENABLE"时为条件可选参数。<br>参数含义：该参数用于设置UNC在PCO信元中响应给终端的Non-IP Link MTU值。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是128~65535。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST LINKMTU查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LINKMTU]] · Link MTU值（LINKMTU）

## 使用实例

配置UNC在PCO信元中携带Link MTU，且响应给终端的IPv4 Link MTU值为300：

```
SET LINKMTU: MTUSW=ENABLE, IPV4LINKMTU=300;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-LINKMTU.md`
