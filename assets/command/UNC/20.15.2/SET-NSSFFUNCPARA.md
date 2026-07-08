---
id: UNC@20.15.2@MMLCommand@SET NSSFFUNCPARA
type: MMLCommand
name: SET NSSFFUNCPARA（设置NSSF数据源以及切片选择流程返回信元）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: NSSFFUNCPARA
command_category: 配置类
applicable_nf:
- NSSF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NSSF业务及策略管理
- NSSF功能参数配置
status: active
---

# SET NSSFFUNCPARA（设置NSSF数据源以及切片选择流程返回信元）

## 功能

**适用NF：NSSF**

该命令用于设置NSSF在业务流程中所使用的数据源与切片选择流程中返回的信元。

## 注意事项

- 该命令执行后立即生效。

- 当DATASOURCETYPE设为ReportData时，切片选择流程会忽略RETURNIETYPE配置，返回CandidateAmfList信元。
- 当前协议动态上报方式不完善，商用部署时数据源设置使用本地配置可用性信息方式。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| DATASOURCETYPE | RETURNIETYPE |
| --- | --- |
| LocalConfigData | TargetAmfSet |

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DATASOURCETYPE | 数据源设置 | 可选必选说明：可选参数<br>参数含义：该参数用于表示NSSF在所有业务流程中使用的数据源是本地配置的切片还是NF上报的切片。<br>数据来源：本端规划<br>取值范围：<br>- LocalConfigData（本地配置可用性信息）<br>- ReportData（AMF上报可用性信息）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCPARA查询当前参数配置值。<br>配置原则：无 |
| RETURNIETYPE | 切片选择返回信元设置 | 可选必选说明：可选参数<br>参数含义：该参数表示NSSF在切片选择流程中给NF返回的信元是CandidateAmfList还是TargetAmfSet。<br>数据来源：本端规划<br>取值范围：<br>- TargetAmfSet（targetAmfSet）<br>- CandidateAmfList（CandidateAmfList ）<br>默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSSFFUNCPARA查询当前参数配置值。<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NSSFFUNCPARA]] · NSSF数据源以及切片选择流程返回信元（NSSFFUNCPARA）

## 使用实例

当运营商想要设置NSSF使用的数据源为本地配置的切片，切片选择流程中的返回信元为TargetAmfSet时，执行此命令：

```
SET NSSFFUNCPARA: DATASOURCETYPE=LocalConfigData, RETURNIETYPE=TargetAmfSet;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-NSSFFUNCPARA.md`
