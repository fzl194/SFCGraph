# 设置NRF国际漫游连接策略（SET NRFCONNPLCY）

- [命令功能](#ZH-CN_MMLREF_0000001176718590__1.3.1)
- [注意事项](#ZH-CN_MMLREF_0000001176718590__1.3.2)
- [参数说明](#ZH-CN_MMLREF_0000001176718590__1.3.4)
- [使用实例](#ZH-CN_MMLREF_0000001176718590__1.3.5)

## [命令功能](#ZH-CN_MMLREF_0000001176718590)

**适用NF：NRF**

设置NRF对接NF/NRF时的国际漫游的连接策略。

## [注意事项](#ZH-CN_MMLREF_0000001176718590)

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PEERNFTYPE | CONNPOLICY |
| --- | --- |
| NRF | DIRECT |
| NF | DIRECT |

#### [操作用户权限](#ZH-CN_MMLREF_0000001176718590)

G_1，管理员级别命令组；G_2，操作员级别命令组

## [参数说明](#ZH-CN_MMLREF_0000001176718590)

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- NF（NF）<br>默认值：无。<br>配置原则：无 |
| CONNPOLICY | 国际漫游连接策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示国际漫游连接策略。<br>数据来源：全网规划<br>取值范围：<br>- “DIRECT（DIRECT）”：与对端NF直接通信，不通过SEPP。<br>- “SBI_TARGET_APIROOT（SBI_TARGET_APIROOT）”：与对端NF通过SEPP交互，在http头中携带对端NF的地址信息。<br>- “HTTP_PROXY（HTTP_PROXY）”：与对端NF通过SEPP交互，在URI中携带对端NF的地址信息。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFCONNPLCY查询当前参数配置值。<br>配置原则：<br>建议本PLMN内NF与SEPP的连接和NRF与SEPP的连接策略保持一致。 |

## [使用实例](#ZH-CN_MMLREF_0000001176718590)

当对端NF类型为NRF时，设置NRF与SEPP的国际漫游连接策略修为SBI_TARGET_APIROOT。

```
SET NRFCONNPLCY: PEERNFTYPE=NRF, CONNPOLICY=SBI_TARGET_APIROOT;
```
