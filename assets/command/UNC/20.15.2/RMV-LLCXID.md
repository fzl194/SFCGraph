---
id: UNC@20.15.2@MMLCommand@RMV LLCXID
type: MMLCommand
name: RMV LLCXID（删除LLC协商参数）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: LLCXID
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
- LLC参数
status: active
---

# RMV LLCXID（删除LLC协商参数）

## 功能

**适用网元：SGSN**

该命令用于删除GB接口LLC层XID协商参数配置。

## 注意事项

- 该命令执行立即生效。
- 可以通过本命令来删除GB接口LLC层XID协商参数N201U，T200的配置。删除配置以后，SGSN主动发起的XID参数协商流程将使用3GPP 44.064定义的缺省值（N201U为500字节，T200为5s（SAPI3），10s（SAPI5），20s（SAPI9），40s（SAPI11））。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAPI | SAPI | 可选必选说明：必选参数<br>参数含义：该参数用于设置SAPI。<br>取值范围：<br>- “SAPI3(SAPI3)”<br>- “SAPI5(SAPI5)”<br>- “SAPI9(SAPI9)”<br>- “SAPI11(SAPI11)”<br>默认值：无<br>说明：SAPI3，SAPI5，SAPI9，SAPI11表示用户数据。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@LLCXID]] · LLC协商参数（LLCXID）

## 使用实例

删除SAPI为3的GB接口LLC层XID协商参数配置：

RMV LLCXID: SAPI=SAPI3;

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-LLCXID.md`
