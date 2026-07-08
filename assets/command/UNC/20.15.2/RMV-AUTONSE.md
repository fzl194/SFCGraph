---
id: UNC@20.15.2@MMLCommand@RMV AUTONSE
type: MMLCommand
name: RMV AUTONSE（删除自动上报的NSE）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: AUTONSE
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
- Gb自动配置管理
- 自动配置维护功能
status: active
---

# RMV AUTONSE（删除自动上报的NSE）

## 功能

![](删除自动上报的NSE(RMV AUTONSE)_72225673.assets/notice_3.0-zh-cn_2.png)

删除AUTONSE将导致NSE相关业务无法使用。

**适用网元：SGSN**

此命令用于删除自动上报的动态Gb over IP的NSE。自动上报的动态Gb over IP的NSE的信息请通过 [**DSP NSE**](../../信令实体管理/显示NSE属性信息（DSP NSE）_26146030.md) 命令查询。

## 注意事项

- 此命令执行后立即生效。
- 此命令会导致删除的NSE的业务被中断。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NSEI | NSE标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定待删除自动上报NSE的网络服务实体标识。<br>取值范围：0～65535<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@AUTONSE]] · 自动上报的NSE（AUTONSE）

## 使用实例

删除 “NSE标识 ” 为 “0” 的自动上报的NSE：

RMV AUTONSE: NSEI=0;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-AUTONSE.md`
