---
id: UNC@20.15.2@MMLCommand@SET NRFNFINFOFMT
type: MMLCommand
name: SET NRFNFINFOFMT（设置NF私有信息格式）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NRFNFINFOFMT
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
- NF私有信息格式管理
status: active
---

# SET NRFNFINFOFMT（设置NF私有信息格式）

## 功能

**适用NF：NRF**

该命令用于设置服务发现、检索响应及通知请求中NF的私有信息字段格式。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE | NFINFOFMT |
| --- | --- |
| BSF | REGFMT |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFTYPE | 网元类型 | 可选必选说明：必选参数<br>参数含义：该参数用于表示设置NF私有信息格式的目标网元类型。<br>数据来源：本端规划<br>取值范围：<br>- BSF（BSF）<br>默认值：无。<br>配置原则：<br>当前只支持设置BSF的私有信息格式。 |
| NFINFOFMT | NF私有信息格式 | 可选必选说明：可选参数<br>参数含义：该参数用于表示服务发现、检索响应及通知请求中NF的私有信息字段格式类型。<br>数据来源：本端规划<br>取值范围：<br>- ARRAY（ARRAY）<br>- REGFMT（REGFMT）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFNFINFOFMT查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [NF私有信息格式（NRFNFINFOFMT）](configobject/UNC/20.15.2/NRFNFINFOFMT.md)

## 使用实例

设置BSF网元的私有信息格式为ARRAY。

```
SET NRFNFINFOFMT:NFTYPE=BSF,NFINFOFMT=ARRAY;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/设置NF私有信息格式（SET-NRFNFINFOFMT）_98288628.md`
