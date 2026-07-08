---
id: UNC@20.15.2@MMLCommand@SET DFTPROXYCTRL
type: MMLCommand
name: SET DFTPROXYCTRL（设置缺省的代理功能）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: DFTPROXYCTRL
command_category: 配置类
applicable_nf:
- SGW-C
- PGW-C
- SMF
effect_mode: 对新用户生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- Proxy SGW_SMF管理
- 缺省代理控制
status: active
---

# SET DFTPROXYCTRL（设置缺省的代理功能）

## 功能

**适用NF：SGW-C、PGW-C、SMF**

该命令用于配置缺省的代理功能。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 该命令只有在PROXYSMFCTRL没有相应配置时才生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| HOMEROUTESW | HOMEITFMODE | DATAHRSW |
| --- | --- | --- |
| OFF | LINK_LEFT | OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| HOMEROUTESW | 支持语音业务回归属地功能开关 | 可选必选说明：可选参数<br>参数含义：该参数用于控制运营商语音业务回归属地。<br>数据来源：本端规划<br>取值范围：<br>- OFF（关闭）<br>- ON（开启）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTPROXYCTRL查询当前参数配置值。<br>配置原则：<br>当DNN是语音业务DNN时该参数生效。开关开启时，IMS语音业务接入时漫游网关作为ProxySMFS8形态对接归属地PGW；开关关闭时，IMS语音业务接入时漫游网关作为N16SMF形态，本地直出SVC。 |
| HOMEITFMODE | 归属地接口模式 | 可选必选说明：可选参数<br>参数含义：该参数用于指示归属地接口模式。<br>数据来源：本端规划<br>取值范围：<br>- “KEEP_S8（保持S8）”：保持S8<br>- “LINK_LEFT（与左侧联动）”：与左侧联动<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTPROXYCTRL查询当前参数配置值。<br>配置原则：<br>当SMF作为ProxySMFS8部署时，配置参数取值为“KEEP_S8(保持S8)”并且SET SMFFUNC的PROSMFS8SUP参数需要配置为“Support(支持)”。当SMF作为ProxySMF部署时， 配置参数取值为“LINK_LEFT(与左侧联动)”。 |
| DATAHRSW | 数据业务回归属地功能开关 | 可选必选说明：该参数在"HOMEITFMODE"配置为"LINK_LEFT"时为条件可选参数。<br>参数含义：该参数用于指示数据业务是否回归属地。<br>数据来源：本端规划<br>取值范围：<br>- “OFF（数据业务回归属地功能关闭）”：数据业务回归属地功能关闭<br>- “ON（数据业务回归属地功能开启）”：数据业务回归属地功能开启<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DFTPROXYCTRL查询当前参数配置值。<br>配置原则：<br>本参数仅在HOMEITFMODE 配置为“LINK_LEFT(与左侧联动)”时生效。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DFTPROXYCTRL]] · 缺省代理控制配置（DFTPROXYCTRL）

## 使用实例

假设运营商需要设置缺省的代理功能，其中语音业务回归属地开关HOMEROUTESW保持关闭，归属地接口模式HOMEITFMODE为“与左侧联动（LINK_LEFT）”，数据业务回归属地功能开关DATAHRSW保持关闭。

```
SET DFTPROXYCTRL: HOMEROUTESW=ON, HOMEITFMODE=LINK_LEFT, DATAHRSW=OFF;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置缺省的代理功能（SET-DFTPROXYCTRL）_21861997.md`
