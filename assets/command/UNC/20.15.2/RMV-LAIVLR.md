---
id: UNC@20.15.2@MMLCommand@RMV LAIVLR
type: MMLCommand
name: RMV LAIVLR（删除LAI与VLR号对应关系）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LAIVLR
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
- 电路域联合业务
- LAI与VLR号对应关系
status: active
---

# RMV LAIVLR（删除LAI与VLR号对应关系）

## 功能

![](删除LAI与VLR号对应关系(RMV LAIVLR)_26145414.assets/notice_3.0-zh-cn_2.png)

删除LAI与VLR的对应关系后，MME将无法找到该LAI所对应的MSC/VLR，CSFallback功能将失效。

**适用网元：SGSN、MME**

该命令用于删除LAI与VLR的对应关系。

## 注意事项

- 该命令执行后立即生效。
- 删除LAI与VLR的对应关系后，MME将无法找到该LAI所对应的MSC/VLR，CSFallback功能将失效。
- LAI和VLR号至少要输入一个。
- 删除LAI与VLR的对应关系时，要确保待删除的LAI区间里的所有LAI均没有被命令[**ADD TAILAI**](../TAI与LAI对应关系/增加TAI与LAI对应关系(ADD TAILAI)_72345017.md)配置，否则不允许删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BGNLAI | LAI | 可选必选说明：可选参数<br>参数说明：该参数用于指定位置区标识，标识一个位置区，由“MCC”、“MNC”和“LAC”组成。<br>数据来源：整网规划<br>取值范围：9~10位字符串<br>默认值：无<br>配置原则：<br>- “MCC”由3个阿拉伯数字组成，“MNC”由2到3个阿拉伯数字组成。<br>- LAC编码为16进制数，固定为4位，不足前面补0。 |
| VLRNO | VLR号 | 可选必选说明：可选参数<br>参数说明：该参数用于指定标识一个VLR。<br>数据来源：整网规划<br>取值范围： 1～15位十进制数字<br>默认值：无<br>配置原则：<br>- “LAI”和“VLR号”至少要输入一个。<br>- 如果只输入“VLR号”，该命令会删除所有与此VLR号相关的LAI与VLR号对应关系的记录。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LAIVLR]] · LAI与VLR号对应关系（LAIVLR）

## 使用实例

1. 删除起始LAI号为"1000009999"的LAI区间与VLR号对应关系：
  输入的起始LAI为"1000009999"，VLR号不输入。
  RMV LAIVLR: BGNLAI="1000009999";
2. 删除VLR号为"100000000000100"所对应的所有LAI的对应关系：
  不输入起始LAI，输入VLR号为"100000000000100"。
  RMV LAIVLR: VLRNO="100000000000100";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除LAI与VLR号对应关系(RMV-LAIVLR)_26145414.md`
