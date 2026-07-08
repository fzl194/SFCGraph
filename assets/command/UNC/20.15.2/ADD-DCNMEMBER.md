---
id: UNC@20.15.2@MMLCommand@ADD DCNMEMBER
type: MMLCommand
name: ADD DCNMEMBER（增加DCN成员）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: DCNMEMBER
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
- DCN成员管理
status: active
---

# ADD DCNMEMBER（增加DCN成员）

## 功能

**适用网元：MME**

当运营商部署DCN时，此命令用于配置DCN所覆盖MME的网络范围。当专用核心网重选时，可通过该配置找到指定DCN下的MME组。执行此命令前需要通过 [**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md) 增加专用核心网。

## 注意事项

- 该命令执行后立即生效。
- 此命令最大记录数为512。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DCN标识。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无<br>配置原则：<br>“DCN ID”<br>已通过<br>[**ADD DCN**](../DCN配置/增加DCN(ADD DCN)_72225505.md)<br>配置，DCN ID可重复。 |
| MMEGI | MME组识别码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置指定DCN的MME组。<br>数据来源：全网规划<br>取值范围：4位16进制编码，范围为0000~FFFF。<br>默认值：无<br>配置原则：同一个DCN ID下的MMEGI不可重叠，但同一个MMEGI可以配置到多个DCN下。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DCNMEMBER]] · DCN成员（DCNMEMBER）

## 使用实例

运营商按照如下方式规划DCN：

1. 增加一个 “DCN ID” 为 “0” 的普通专用核心网：
  ADD DCN: DCNID=0, MCC="123", MNC="01", DCNTYPE=COMMON, DESC="eMtc";
2. 将 “MMEGI” 为 “A1B3” 的MME组划分到 “DCN ID” 为 “0” 的网络中：
  ADD DCNMEMBER: DCNID=0, MMEGI="A1B3";
3. 增加DCN映射关系，使在专用核心网重选中范围在 “150” 至 “180” 的UE USAGE TYPE映射到 “DCN ID” 为 “0” 的DCN网络中：
  ADD DCNMAP: DCNID=0, BGNUEUSAGETYPE=150, ENDUEUSAGETYPE=180;

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-DCNMEMBER.md`
