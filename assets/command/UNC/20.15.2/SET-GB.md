---
id: UNC@20.15.2@MMLCommand@SET GB
type: MMLCommand
name: SET GB（设置Gb通用信息）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: GB
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- Gb通用信息参数
status: active
---

# SET GB（设置Gb通用信息）

## 功能

![](设置Gb通用信息(SET GB)_72225685.assets/notice_3.0-zh-cn_2.png)

GB OVER IP自动配置功能开启后再关闭有可能影响业务。

**适用网元：SGSN**

此命令用于设置Gb over IP的相关信息，包括：资源重分配功能，Gb over IP动态自动配置功能，Gb over IP的UDP校验功能。

## 注意事项

- 系统初次运行时，会执行系统初始设置值。
- 该命令执行后立即生效。
- GB OVER IP自动配置功能开启后再关闭有可能影响业务。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| GIRD | 启用Gb over IP资源分配功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用Gb over IP资源重分配功能。<br>数据来源：整网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>系统初始设置值：<br>“NO(否)”<br>说明：如果参数设为"YES"，允许PCU(或SGSN)显式地改变数据的接收端的IP地址和端口号，可以有效地抑制拥塞，因此建议参数设置为"YES"。关于资源重分配的具体描述，可参考协议48016。由BSC主导是否开启该功能，只有当BSC和<br>UNC<br>两端都开启该功能的时候该功能才能正常使用。 |
| AUTO | 启用Gb动态 over IP自动配置功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用Gb动态 over IP自动配置功能。<br>数据来源：整网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>系统初始设置值：<br>“NO(否)”<br>说明：如果参数设为"YES"，<br>UNC<br>根据PCU上报的NSE信息自动生成本地NSE配置数据。 |
| UDPCHK | 启用Gb over IP接口UDP校验功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指定是否使用Gb over IP接口的UDP校验功能。<br>数据来源：整网规划<br>取值范围：<br>- YES(是)<br>- NO(否)<br>系统初始设置值：<br>“YES(是)”<br>说明：如果参数设为"YES"，<br>UNC<br>发送的该接口报文UDP校验字段有效（值非零），会丢弃UDP校验错误的接收报文，因此可能会增加整系统的丢包率。参与UDP校验的报文包括：NS层管理报文、BSSGP层管理报文、MS用户的信令报文。 系统默认开启此功能。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/GB]] · Gb通用信息（GB）

## 使用实例

启用Gb over IP资源分配和Gb over IP接口UDP校验功能，不启用Gb动态 over IP自动配置功能：

SET GB: GIRD=YES, AUTO=NO, UDPCHK=YES;

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-GB.md`
