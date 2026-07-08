---
id: UNC@20.15.2@MMLCommand@RMV SPECRFSPVALUE
type: MMLCommand
name: RMV SPECRFSPVALUE（删除特征RFSP取值）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: SPECRFSPVALUE
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
- 移动性管理
- RFSP管理
- 特征RFSP管理
- 特征RFSP取值范围管理
status: active
---

# RMV SPECRFSPVALUE（删除特征RFSP取值）

## 功能

**适用网元：SGSN、MME**

该命令用于把一组RFSP从特征RFSP(RAT/Frequency Selection Priority)中删除。

## 注意事项

此命令执行后立即生效。

此命令执行后起始RFSP对应的整条记录都将被删除。

如果待删除的 “RFSPIDX(特征RFSP索引)” “RFSPIDX(特征RFSP索引)” 被其他命令引用，则该 “RFSPIDX(特征RFSP索引)” 下至少保留一条记录。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RFSPIDX | 特征RFSP索引 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要被删除的特征RFSP索引，该索引标识了一组RFSP取值。<br>数据来源：本端规划<br>取值范围：0~49<br>默认值：无 |
| BEGRFSP | 起始RFSP | 可选必选说明：必选参数<br>参数含义：该参数用于指定一段连续特征RFSP的起始值。<br>取值范围：1~256<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SPECRFSPVALUE]] · 特征RFSP取值（SPECRFSPVALUE）

## 使用实例

把一组RFSP从特征RFSP(RAT/Frequency Selection Priority)中删除：

RMV SPECRFSPVALUE: RFSPIDX=0, BEGRFSP=1;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-SPECRFSPVALUE.md`
