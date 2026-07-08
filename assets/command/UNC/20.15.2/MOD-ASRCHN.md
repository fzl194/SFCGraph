---
id: UNC@20.15.2@MMLCommand@MOD ASRCHN
type: MMLCommand
name: MOD ASRCHN（修改容灾业务通道配置）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: ASRCHN
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
- 网络管理
- 主备容灾管理
- 容灾业务通道
status: active
---

# MOD ASRCHN（修改容灾业务通道配置）

## 功能

**适用网元：SGSN、MME**

该命令已废弃。

此命令用于修改容灾业务通道的检测参数。

## 注意事项

该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHNID | 容灾业务通道ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定容灾业务通道ID。<br>数据来源：本端规划<br>取值范围：0<br>默认值：无 |
| DETITERVAL | 探测报文发送周期 （毫秒） | 可选必选说明：可选参数<br>参数含义：该参数用于指定在容灾业务通道上发送探测报文的时间间隔。<br>数据来源：本端规划<br>取值范围：200～1000<br>默认值：无 |
| DETTIMES | 探测报文重传次数 | 可选必选说明：可选参数<br>参数含义：该参数用于指定在容灾业务通道上发送一条探测报文的最大尝试次数。<br>数据来源：本端规划<br>取值范围：1～60<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ASRCHN]] · 容灾业务通道配置（ASRCHN）

## 使用实例

修改 “容灾业务通道ID” 为 “0” 的容灾业务通道，修改 “探测报文发送周期 （毫秒）” 为 “500” ， “探测报文重传次数” 为 “25” 。

MOD ASRCHN: CHNID=0, DETITERVAL=500, DETTIMES=25;

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-ASRCHN.md`
