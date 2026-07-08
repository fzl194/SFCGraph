---
id: UNC@20.15.2@MMLCommand@ADD DCNMAP
type: MMLCommand
name: ADD DCNMAP（增加DCN映射关系）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DCNMAP
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
max_records: 512
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN映射关系
status: active
---

# ADD DCNMAP（增加DCN映射关系）

## 功能

**适用网元：MME**

当部署DCN时，此命令用于根据用户的签约数据UE Usage Type配置指定DCN所服务的用户范围。UE Usage Type表示UE的使用特征，根据UE Usage Type可以选择特定的专用核心网。执行此命令前需要通过 [**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md) 增加专用核心网。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为512。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定DCN ID。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：<br>- “DCN ID”必须已通过[**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md)配置。<br>- 一个DCN ID可配置多条记录。 |
| BGNUEUSAGETYPE | 起始UE USAGE TYPE | 可选必选说明：必选参数<br>参数含义：该参数用于指定起始UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：相同PLMN下的UE Usage Type范围不可以重叠。 |
| ENDUEUSAGETYPE | 终止UE USAGE TYPE | 可选必选说明：可选参数<br>参数含义：该参数用于指定终止UE USAGE TYPE。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：<br>- 相同PLMN下的UE Usage Type范围不可以重叠。<br>- “终止UE Usage Type”必须大于等于“起始UE Usage Type”。<br>- 如果该参数未输入，取值与“起始UE Usage Type”相同。 |

## 操作的配置对象

- [DCN映射关系（DCNMAP）](configobject/UNC/20.15.2/DCNMAP.md)

## 使用实例

运营商按照如下方式规划DCN：

1. 增加一个 “DCN ID” 为 “0” 的普通专用核心网：
  ADD DCN: DCNID=0, MCC="123", MNC="01", DCNTYPE=COMMON, DESC="eMtc";
2. 将 “MMEGI” 为 “A1B3” 的MME组划分到 “DCN ID” 为 “0” 的网络中：
  ADD DCNMEMBER: DCNID=0, MMEGI="A1B3";
3. 增加DCN映射关系，使在专用核心网重选中范围在 “150” 至 “180” 的UE USAGE TYPE映射到 “DCN ID” 为 “0” 的DCN网络中：
  ADD DCNMAP: DCNID=0, BGNUEUSAGETYPE=150, ENDUEUSAGETYPE=180;

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加DCN映射关系(ADD-DCNMAP)_26305638.md`
