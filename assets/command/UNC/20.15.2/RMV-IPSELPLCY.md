---
id: UNC@20.15.2@MMLCommand@RMV IPSELPLCY
type: MMLCommand
name: RMV IPSELPLCY（删除IP地址选择策略）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPSELPLCY
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
- IP地址选择策略
status: active
---

# RMV IPSELPLCY（删除IP地址选择策略）

## 功能

**适用网元：SGSN、MME**

该命令用于删除S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口IP地址选择策略。

## 注意事项

- 该命令执行后立即生效。
- 删除“DEFAULT(缺省策略)”，则S10、S11、Gn/Gp、S5/S8、S3、S4、Sv接口按IPv4策略来选。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CTRLRANGE | 控制范围 | 可选必选说明：必选参数<br>参数含义：该参数用于指定命令生效的范围。<br>数据来源：整网规划<br>取值范围：<br>- “DEFAULT(缺省策略)”<br>- “SPECIFY(指定IMSI)”<br>默认值：无 |
| IMSI | IMSI | 可选必选说明：条件必选参数<br>参数含义：该参数用于指定用户的IMSI。<br>前提条件：该参数在<br>“CTRLRANGE(控制范围)”<br>设置为<br>“SPECIFY(指定IMSI)”<br>有效。<br>数据来源：整网规划<br>取值范围：1~15位十进制数字<br>默认值：无 |

## 操作的配置对象

- [IP地址选择策略（IPSELPLCY）](configobject/UNC/20.15.2/IPSELPLCY.md)

## 使用实例

删除其中一个测试用户：

RMV IPSELPLCY: CTRLRANGE=SPECIFY, IMSI="123031501000001";

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP地址选择策略(RMV-IPSELPLCY)_72345059.md`
