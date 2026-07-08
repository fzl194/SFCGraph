---
id: UNC@20.15.2@MMLCommand@MOD DMLE
type: MMLCommand
name: MOD DMLE（修改Diameter本端实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMLE
command_category: 配置类
applicable_nf:
- SGSN
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter本地实体
status: active
---

# MOD DMLE（修改Diameter本端实体）

## 功能

**适用网元：SGSN、MME**

该命令用于修改Diameter本端实体信息。Diameter协议用于支持MME与HSS（Home Subscriber Server）传递签约及鉴权数据以授权用户接入EPS网络。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定准备修改的本地实体的索引。<br>数据来源：整网规划<br>取值范围：0～31<br>默认值：无 |
| PDTNAME | 产品名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定产品名，用于标识本端产品信息。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：该参数用来标识本端的产品信息，一般可直接填写产品的名称。如填写MME。 |
| LOINFONAME | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定本地实体名称，标示本地实体。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：用来标识本地实体时，一般配置为DMLE。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DMLE]] · Diameter本端实体（DMLE）

## 使用实例

修改索引为0的实体记录，产品名修改为MME1，本地实体名修改为DMLE：

MOD DMLE: LOINDEX=0, PDTNAME="MME1", LOINFONAME="DMLE";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter本端实体(MOD-DMLE)_72225961.md`
