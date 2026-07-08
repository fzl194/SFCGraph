---
id: UNC@20.15.2@MMLCommand@MOD DMVLE
type: MMLCommand
name: MOD DMVLE（修改Diameter虚拟本地实体）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: DMVLE
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- Diameter管理
- Diameter虚拟本地实体
status: active
---

# MOD DMVLE（修改Diameter虚拟本地实体）

## 功能

**适用网元：MME**

该命令用于修改Diameter虚拟本地实体的 “产品名” 和 “本地实体名” 。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOINDEX | 本地实体索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定虚拟本地实体的索引，在Diameter链路中唯一标识一个虚拟本地实体。<br>数据来源：本端规划<br>取值范围：32~63<br>默认值：无 |
| PDTNAME | 产品名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定产品名，用于标识本端产品信息。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：该参数用来标识本端的产品信息，一般可直接填写产品的名称。如填写<br>UNC<br>。 |
| LOINFONAME | 本地实体名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定虚拟本地实体名称，标识虚拟本地实体。<br>数据来源：本端规划<br>取值范围：0～32位字符串<br>默认值：无<br>配置原则：用来标识虚拟本地实体时，一般配置为DMVLE。 |

## 操作的配置对象

- [Diameter虚拟本地实体（DMVLE）](configobject/UNC/20.15.2/DMVLE.md)

## 使用实例

修改索引为32的实体记录，产品名修改为MME1，本地实体名修改为DMVLE：

MOD DMVLE: LOINDEX=32, PDTNAME="MME1", LOINFONAME="DMVLE";

## 证据

- 原始手册：`evidence/UNC/20.15.2/修改Diameter虚拟本地实体(MOD-DMVLE)_26306108.md`
