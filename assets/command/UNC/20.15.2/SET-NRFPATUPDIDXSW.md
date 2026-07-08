---
id: UNC@20.15.2@MMLCommand@SET NRFPATUPDIDXSW
type: MMLCommand
name: SET NRFPATUPDIDXSW（设置PATCH更新携带下标处理开关）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFPATUPDIDXSW
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 对端NF管理
- NF信息管理
- PATCH更新携带下标处理开关
status: active
---

# SET NRFPATUPDIDXSW（设置PATCH更新携带下标处理开关）

## 功能

**适用NF：NRF**

该命令用于配置NF PATCH更新，更新的信元路径是否可以携带下标，因NF PATCH更新时，如果PatchItem patch中使用下标，用下标来指定要更新的数组元素的位置，则拒绝此类更新。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需配置且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| PATUPDWITHIDXSW |
| --- |
| FUNC_OFF |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PATUPDWITHIDXSW | 禁止PATCH更新携带下标开关 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NF到NRF进行PATCH更新时更新的信元路径是否可以携带下标。若开关设置为“FUNC_ON”，则更新的信元路径禁止携带下标；若开关设置为“FUNC_OFF”，则更新的信元路径允许携带下标。<br>数据来源：本端规划<br>取值范围：<br>- FUNC_ON（打开）<br>- FUNC_OFF（关闭）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFPATUPDIDXSW查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFPATUPDIDXSW]] · PATCH更新携带下标处理开关（NRFPATUPDIDXSW）

## 使用实例

配置NF PATCH更新，更新的信元路径禁止携带下标，设置PATUPDWITHIDXSW为开。

```
SET NRFPATUPDIDXSW:PATUPDWITHIDXSW = FUNC_ON;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NRFPATUPDIDXSW.md`
