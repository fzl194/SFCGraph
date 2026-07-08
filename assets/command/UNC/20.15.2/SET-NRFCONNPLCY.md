---
id: UNC@20.15.2@MMLCommand@SET NRFCONNPLCY
type: MMLCommand
name: SET NRFCONNPLCY（设置NRF国际漫游连接策略）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFCONNPLCY
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- NRF业务参数
- NRF国际漫游参数管理
status: active
---

# SET NRFCONNPLCY（设置NRF国际漫游连接策略）

## 功能

**适用NF：NRF**

设置NRF对接NF/NRF时的国际漫游的连接策略。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PEERNFTYPE | CONNPOLICY |
| --- | --- |
| NRF | DIRECT |
| NF | DIRECT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PEERNFTYPE | 对端NF类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示对端NF类型。<br>数据来源：本端规划<br>取值范围：<br>- NRF（NRF）<br>- NF（NF）<br>默认值：无。<br>配置原则：无 |
| CONNPOLICY | 国际漫游连接策略 | 可选必选说明：可选参数<br>参数含义：该参数用于表示国际漫游连接策略。<br>数据来源：全网规划<br>取值范围：<br>- “DIRECT（DIRECT）”：与对端NF直接通信，不通过SEPP。<br>- “SBI_TARGET_APIROOT（SBI_TARGET_APIROOT）”：与对端NF通过SEPP交互，在http头中携带对端NF的地址信息。<br>- “HTTP_PROXY（HTTP_PROXY）”：与对端NF通过SEPP交互，在URI中携带对端NF的地址信息。<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFCONNPLCY查询当前参数配置值。<br>配置原则：<br>建议本PLMN内NF与SEPP的连接和NRF与SEPP的连接策略保持一致。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFCONNPLCY]] · NRF国际漫游连接策略（NRFCONNPLCY）

## 使用实例

当对端NF类型为NRF时，设置NRF与SEPP的国际漫游连接策略修为SBI_TARGET_APIROOT。

```
SET NRFCONNPLCY: PEERNFTYPE=NRF, CONNPOLICY=SBI_TARGET_APIROOT;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFCONNPLCY.md`
