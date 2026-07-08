---
id: UNC@20.15.2@MMLCommand@RMV S1USRSECPARA
type: MMLCommand
name: RMV S1USRSECPARA（删除S1模式用户安全配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: S1USRSECPARA
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
- 用户安全管理
- S1模式用户安全参数
status: active
---

# RMV S1USRSECPARA（删除S1模式用户安全配置）

## 功能

![](删除S1模式用户安全配置(RMV S1USRSECPARA)_72345247.assets/notice_3.0-zh-cn_2.png)

如果执行该命令可能导致加密算法或者完整性算法生效变化，导致终端接入异常。

**适用网元：MME**

此命令用于删除指定号段的用户的鉴权、加密、完整性保护等安全配置。

## 注意事项

- 此命令只能删除特定IMSI前缀的安全配置，而不能删除全系统默认的安全配置。
- 此命令对于当前系统内已存在签约数据的用户不立即生效，在用户签约数据被删除后再次进行附着时开始生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| IMSIPRE | IMSI前缀 | 可选必选说明：必选参数<br>参数含义：待删除的特定用户群对应的IMSI前缀。<br>取值范围：5~15位数字<br>默认值：无<br>说明：特定用户群安全配置被删除后，该部分用户使用系统默认的安全配置。 |

## 操作的配置对象

- [S1模式用户安全配置（S1USRSECPARA）](configobject/UNC/20.15.2/S1USRSECPARA.md)

## 使用实例

删除IMSI前缀为3080102的用户群的安全配置：

RMV S1USRSECPARA: IMSIPRE="3080102";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除S1模式用户安全配置(RMV-S1USRSECPARA)_72345247.md`
