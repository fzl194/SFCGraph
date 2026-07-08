---
id: UNC@20.15.2@MMLCommand@MOD LLCXID
type: MMLCommand
name: MOD LLCXID（修改LLC协商参数）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: LLCXID
command_category: 配置类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- Gb接口管理
- LLC参数
status: active
---

# MOD LLCXID（修改LLC协商参数）

## 功能

**适用网元：SGSN**

该命令用来修改GB接口LLC层XID协商参数配置。

## 注意事项

可以通过该命令来修改之前通过 [**ADD LLCXID**](增加LLC协商参数(ADD LLCXID)_72345615.md) 命令增加的XID参数N201U，T200配置。SGSN为后续接入的用户使用新的XID参数配置进行协商。如果之前没有为某个SAPI配置过XID参数，请先使用 [**ADD LLCXID**](增加LLC协商参数(ADD LLCXID)_72345615.md) 增加配置。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SAPI | SAPI | 可选必选说明：必选参数<br>参数含义：该参数用于表示SAPI。<br>数据来源：整网规划<br>取值范围：<br>- “SAPI3(SAPI3)”<br>- “SAPI5(SAPI5)”<br>- “SAPI9(SAPI9)”<br>- “SAPI11(SAPI11)”<br>默认值：无<br>说明：SAPI3，SAPI5，SAPI9，SAPI11表示用户数据。 |
| N201U | SN-UNITDATA PDU最大字节数 | 可选必选说明：可选参数<br>参数含义：该参数用于设置U帧的信息域最大长度。<br>数据来源：整网规划<br>取值范围：140～1520<br>默认值：无 |
| T200 | LLC重传定时器（s） | 可选必选说明：可选参数<br>参数含义：该参数用于设置LLC层重传定时器时长。<br>数据来源：整网规划<br>取值范围：5s～40s<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LLCXID]] · LLC协商参数（LLCXID）

## 使用实例

修改SAPI3的配置N201U为1520，T200为40秒：

MOD LLCXID: SAPI=SAPI3, N201U=1520, T200=40;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-LLCXID.md`
