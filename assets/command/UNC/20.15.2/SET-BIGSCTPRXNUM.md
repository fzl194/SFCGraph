---
id: UNC@20.15.2@MMLCommand@SET BIGSCTPRXNUM
type: MMLCommand
name: SET BIGSCTPRXNUM（设置大端模式SCTP接收缓冲区参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: BIGSCTPRXNUM
command_category: 配置类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET BIGSCTPRXNUM（设置大端模式SCTP接收缓冲区参数）

## 功能

![](设置大端模式SCTP接收缓冲区参数(SET BIGSCTPRXNUM)_26238016.assets/notice_3.0-zh-cn_2.png)

修改参数需要复位SGP进程才能生效，如果配置不合理会导致进程启动故障。

**适用网元：MME**

该命令用于设置大端模式SCTP接收缓冲区参数。缓冲区分为大缓冲区和小缓冲区，缓冲区分块规格包含max块、med块和min块。使用大缓冲区的接口有Iu（M3UA协议）、S6a/S6d（Diameter协议）、SBc、SGs和SLs；使用小缓冲区的接口有S1-MME和N2。SCTP会将接收到的报文根据大小存放到合适的块内。该命令只控制使用大缓冲区的max块个数。

该命令的使用场景：当CBC发送的消息超过64K时，可通过本命令设置SCTP接收缓冲区参数以支持MME处理大规格消息。

## 注意事项

- 该命令执行后需要重启SGP进程（LINK RU或者LINK VNFC）才能生效。
- 该命令会影响SCTP内存分布。
- 该命令需要配合设置SCTP缓冲区模式[**SET SCTPBUFFERMODE**](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)使用。
- 该命令配置的参数仅在[**SET SCTPBUFFCFG**](设置SCTP缓冲区参数源(SET SCTPBUFFCFG)_03932862.md)的“SCTP缓冲区参数源类型”设置为“SYSTEM（系统内置）”时才会生效。
- 使用该命令设置大端模式SCTP接收缓冲区参数时，大端模式SCTP接收缓冲区总量不能超过76708800字节，总量 = (“私有模式max块数目”* 私有模式max块大小（1610字节） + 私有模式med块数目(850) * 私有模式med块大小(350字节) + 私有模式min块数目(280) * 私有模式min块大小(150字节)) *“私有模式耦连个数”。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BIGMAXBFNUM | 私有模式max块数目 | 可选必选说明：可选参数。<br>参数含义：当使用命令<br>[**SET SCTPBUFFERMODE**](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)<br>设置<br>“接收端缓冲区模式”<br>为<br>“PRIVATE（私有模式）”<br>时，该参数表示大缓冲区max块在单进程中的块数量。<br>数据来源：全网规划<br>取值范围：0-500<br>系统初始设置值：120<br>配置原则：当需要开启大包处理功能，打开<br>[**SET SBCFUNC**](../../SBc接口管理/SBc参数/设置小区广播功能(SET SBCFUNC)_26306190.md)<br>的<br>“大包处理功能开关”<br>，建议本参数设置为372。 |
| BIGPRIASSNUM | 私有模式耦连个数 | 可选必选说明：可选参数。<br>参数含义：当使用命令<br>[**SET SCTPBUFFERMODE**](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)<br>设置<br>“接收端缓冲区模式”<br>为<br>“PRIVATE（私有模式）”<br>时，该参数表示大缓冲区单进程中的耦连个数。<br>数据来源：全网规划<br>取值范围：0-1000<br>系统初始设置值：144<br>配置原则：当需要开启大包处理功能，打开<br>[**SET SBCFUNC**](../../SBc接口管理/SBc参数/设置小区广播功能(SET SBCFUNC)_26306190.md)<br>的<br>“大包处理功能开关”<br>，建议本参数设置为81。 |
| BIGSHAMAXBFNUM | 共享模式max块数目 | 可选必选说明：可选参数。<br>参数含义：当使用命令<br>[**SET SCTPBUFFERMODE**](设置SCTP缓冲区模式(SET SCTPBUFFERMODE)_04252670.md)<br>设置<br>“接收端缓冲区模式”<br>为<br>“SHARE（共享模式）”<br>时，该参数表示大缓冲区max缓存区单偶联的使用上限<br>数据来源：全网规划<br>取值范围：72-1000<br>系统初始设置值：120<br>配置原则：当需要开启大包处理功能，打开<br>[**SET SBCFUNC**](../../SBc接口管理/SBc参数/设置小区广播功能(SET SBCFUNC)_26306190.md)<br>的<br>“大包处理功能开关”<br>，建议本参数设置为372。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@BIGSCTPRXNUM]] · 大端模式SCTP接收缓冲区参数（BIGSCTPRXNUM）

## 使用实例

设置大端模式SCTP接收缓冲区参数 “私有模式max块数目” 为120， “私有模式耦连个数” 为144， “共享模式max块数目” 为120：

```
SET BIGSCTPRXNUM: BIGMAXBFNUM=120, BIGPRIASSNUM=144, BIGSHAMAXBFNUM=120;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-BIGSCTPRXNUM.md`
