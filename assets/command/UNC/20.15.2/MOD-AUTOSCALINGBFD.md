---
id: UNC@20.15.2@MMLCommand@MOD AUTOSCALINGBFD
type: MMLCommand
name: MOD AUTOSCALINGBFD（修改BFD会话自动化配置模板）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: AUTOSCALINGBFD
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 自动部署
- BFD会话自动化配置
status: active
---

# MOD AUTOSCALINGBFD（修改BFD会话自动化配置模板）

## 功能

该命令用于修改BFD会话自动化配置模板。

## 注意事项

- 该命令执行后立即生效。
- 修改该模板时，要保证该模板添加过。
- 该命令在自动化配置开关为关闭的状态下才能执行，请先使用SET AUTOCONFIG命令关闭自动配置开关；生效配置，需要再次使用SET AUTOCONFIG命令开启自动配置开关。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TEMPLATENAME | 模板名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定BFD自动化配置模板名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～59。不支持空格和中文。<br>默认值：无 |
| BFDTYPE | BFD类型 | 可选必选说明：必选参数<br>参数含义：该参数用来表示BFD自动化配置模板类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Static：该模板是静态BFD自动化配置模板。<br>- Dynamic：该模板是动态BFD自动化配置模板。<br>默认值：无 |
| SERVICENAME | 服务名称 | 可选必选说明：条件必选参数<br>前提条件：该参数在“BFDTYPE”配置为“Static”时为必选参数。<br>参数含义：该参数用来表示接口自动化配置服务模板名称。要求和ADD AUTOSCALINGSERVICE命令中配置的SERVICENAME参数保持一致。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。不支持空格和中文。<br>默认值：无<br>配置原则：该参数不能修改。 |
| IPVERSION | IP版本 | 可选必选说明：条件必选参数<br>前提条件：该参数在“BFDTYPE”配置为“Static”时为必选参数。<br>参数含义：该参数用来表示IP版本。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IPv4：IPv4地址族。<br>- IPv6：IPv6地址族。<br>默认值：无<br>配置原则：该参数不支持修改。 |
| DESTADDR4 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。<br>参数含义：该参数用于表示IPv4目的地址。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。<br>默认值：无 |
| DESTADDR6 | 目的地址 | 可选必选说明：条件必选参数<br>前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。<br>参数含义：该参数用于表示IPv6目的地址。<br>数据来源：对端协商<br>取值范围：IPv6地址类型。<br>默认值：无 |
| MINECHORXINT | 单臂Echo会话的收包间隔（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“BFDTYPE”配置为“Static”时为可选参数。<br>参数含义：该参数用于表示单臂Echo会话的收包间隔（ms）。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| MINRXINTERVAL | 动态BFD会话的收包间隔（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“BFDTYPE”配置为“Dynamic”时为可选参数。<br>参数含义：该参数用于表示动态BFD会话的收包间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| MINTXINTERVAL | 动态BFD会话的发包间隔（ms） | 可选必选说明：条件可选参数<br>前提条件：该参数在“BFDTYPE”配置为“Dynamic”时为可选参数。<br>参数含义：该参数用于表示动态BFD会话的发包间隔。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为30～1000，单位是毫秒。<br>默认值：无 |
| DETECTMULTI | 检测倍数 | 可选必选说明：可选参数<br>参数含义：该参数用于表示检测倍数，如果BFD会话在设置的检测周期内没有收到对端发来的BFD报文，则认为链路发生了故障，BFD会话的状态将会置为Down。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为3～50。<br>默认值：无 |
| ONEARMECHO | 单臂Echo | 可选必选说明：条件可选参数<br>前提条件：该参数在“BFDTYPE”配置为“Static”时为可选参数。<br>参数含义：该参数用于指定是否是单臂echo功能BFD会话。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- TRUE：BFD会话是单臂Echo会话。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AUTOSCALINGBFD]] · BFD会话自动化配置模板（AUTOSCALINGBFD）

## 使用实例

- 修改一个动态BFD会话自动化配置模板：
  ```
  MOD AUTOSCALINGBFD:TEMPLATENAME="bfdtemp",BFDTYPE=Dynamic,DETECTMULTI=40,MINRXINTERVAL=200,MINTXINTERVAL=200;
  ```
- 修改一个静态BFD会话自动化配置模板：
  ```
  MOD AUTOSCALINGBFD:TEMPLATENAME="bfdtemp",SERVICENAME="bfdtemp",BFDTYPE=Static,IPVERSION=IPv4,DESTADDR4="10.1.1.100", MINECHORXINT=200,DETECTMULTI=40,ONEARMECHO=TRUE;
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-AUTOSCALINGBFD.md`
