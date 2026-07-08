---
id: UNC@20.15.2@MMLCommand@RMV DCNMEMBER
type: MMLCommand
name: RMV DCNMEMBER（删除DCN成员）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: DCNMEMBER
command_category: 配置类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 业务安全管理
- DCN管理
- DCN成员管理
status: active
---

# RMV DCNMEMBER（删除DCN成员）

## 功能

**适用网元：MME**

该命令用于删除指定DCN下的MME组成员。删除后，当专用核心网重选时，DCN将不能重选至被删除的MME组。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DCNID | DCN ID | 可选必选说明：必选参数<br>参数含义：该参数用来指定DCN标识。<br>数据来源：全网规划<br>取值范围：0~255<br>默认值：无 |
| MMEGI | MME组识别码 | 可选必选说明：必选参数<br>参数含义：该参数用于配置指定DCN的MME组。<br>数据来源：全网规划<br>取值范围：4位16进制编码，范围为0000~FFFF。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/DCNMEMBER]] · DCN成员（DCNMEMBER）

## 使用实例

运营商调整规划不再将 “MMEGI” 为 “A1B3” 的MME组成员划分到 “DCN ID” 为 “0” 的DCN下：

RMV DCNMEMBER: DCNID=0, MMEGI="A1B3";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除DCN成员(RMV-DCNMEMBER)_72345431.md`
