---
id: UNC@20.15.2@MMLCommand@RMV CHGPLMNCG
type: MMLCommand
name: RMV CHGPLMNCG（删除PLMN-CG配置参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: CHGPLMNCG
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 计费管理
- PLMN CG 配置
status: active
---

# RMV CHGPLMNCG（删除PLMN-CG配置参数）

## 功能

![](删除PLMN-CG配置参数(RMV CHGPLMNCG)_26305202.assets/notice_3.0-zh-cn_2.png)

执行后影响新激活用户。

**适用网元：SGSN**

该命令用于删除为PLMN配置的CG IP地址。如果没有为某个PLMN配置CG IP地址，SGSN会将该PLMN的话单发给其他链路正常的CG，并优先选择CG配置表中 “PLMNFLG” 属性为 “NO” 的CG。请参见 [**ADD CHGCG**](../计费控制/增加CG配置参数（ADD CHGCG）_72225055.md) 命令说明。

## 注意事项

- 该命令执行后立即生效。 执行后影响新激活用户。
- 删除PLMN-CG配置参数后，请检查相关CG的配置是否需要删除。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MCC | 移动国家码 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PLMN的移动国家号码。<br>取值范围：位数为3的十进制数字<br>默认值：无 |
| MNC | 移动网号 | 可选必选说明：必选参数<br>参数含义：该参数用于表示PLMN的移动网号码。<br>取值范围：位数为2或3的十进制数字<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CHGPLMNCG]] · PLMN-CG配置参数（CHGPLMNCG）

## 使用实例

删除PLMN为123001的优先发送话单的CG IP地址：

RMV CHGPLMNCG: MCC="123", MNC="001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除PLMN-CG配置参数(RMV-CHGPLMNCG)_26305202.md`
