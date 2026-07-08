---
id: UNC@20.15.2@MMLCommand@SET SCTPCCTRLPARA
type: MMLCommand
name: SET SCTPCCTRLPARA（设置RAN侧拥塞检测功能参数）
nf: UNC
version: 20.15.2
verb: SET
object_keyword: SCTPCCTRLPARA
command_category: 配置类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SCTP管理
status: active
---

# SET SCTPCCTRLPARA（设置RAN侧拥塞检测功能参数）

## 功能

**适用网元：MME、AMF**

该命令用于配置SCTP链路拥塞控制相关参数信息。

## 注意事项

- 该命令执行后立即生效。

## 权限

manage-ug；system-ug
G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTRLSW | 拥塞控制功能 | 可选必选说明：可选参数<br>参数含义：该参数用于指示是否开启RAN侧SCTP层拥塞控制功能。<br>数据来源：本端规划<br>取值范围：<br>- “ON(开启)”<br>- “OFF(关闭)”<br>系统初始设置值：<br>“OFF(关闭)” |
| CCTRLALGTYPE | 拥塞控制算法 | 可选必选说明：条件可选参数<br>参数含义：该参数用于指定进行RAN侧SCTP层链路拥塞控制算法。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>后生效。<br>数据来源：本端规划<br>取值范围：<br>“BBR（BBR拥塞控制算法）”<br>系统初始设置值：<br>“BBR（BBR拥塞控制算法）”<br>配置原则：当前仅支持BBR拥塞控制算法并且对S1、N2接口同时生效。<br>说明：配置<br>“BBR（BBR拥塞控制算法）”<br>后，<br>[**SET S1APPARA**](../../S1接口管理/S1AP协议参数/设置S1AP协议参数(SET S1APPARA)_72225935.md)<br>命令的<br>“CCTRL（拥塞控制功能）”<br>参数控制的CUBIC拥塞控制功能不生效。 |
| LOWOVLTHD | 低优先级消息流控时延（ms） | 可选必选说明：条件可选参数<br>参数含义：SCTP缓存中消息积压时延大于低优先级消息流控时延时，低优先级消息会被流控。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：10~65535<br>系统初始设置值：300<br>配置原则：<br>“低优先级消息流控时延（ms）”<br>的配置值应小于<br>“高优先级消息流控时延（ms）”<br>的配置值。 |
| HIGHOVLTHD | 高优先级消息流控时延（ms） | 可选必选说明：条件可选参数<br>参数含义：SCTP缓存中消息积压时延大于高优先级消息流控时延时，低优先级消息和高优先级消息均会被流控。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：10~65535<br>系统初始设置值：450<br>配置原则：<br>“高优先级消息流控时延（ms）”<br>的配置值应大于<br>“低优先级消息流控时延（ms）”<br>的配置值。 |
| TXCACHEOVLTHD | 发送缓存过载时延（ms） | 可选必选说明：条件可选参数<br>参数含义：SCTP缓存中消息积压时延大于发送缓存过载时延时，该SCTP链路进入拥塞控制状态。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：10~65535<br>系统初始设置值：800<br>配置原则：<br>“发送缓存过载时延（ms）”<br>的配置值应大于<br>“发送缓存过载恢复时延（ms）”<br>的配置值。 |
| TXCACHEOVLNUM | 连续过载次数（个） | 可选必选说明：条件可选参数<br>参数含义：过载检测周期40ms，当连续过载次数大于此阈值时，进入流控状态。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~255<br>系统初始设置值：5<br>配置原则：配置值越小越容易触发BBR拥塞控制流控，配置值越大拥塞控制效果越不明显。 |
| TXCACHERESTHD | 发送缓存过载恢复时延（ms） | 可选必选说明：条件可选参数<br>参数含义：SCTP发送缓存消息积压时延小于等于发送缓存过载恢复时延，该SCTP链路恢复正常状态，正常状态持续一段时间（通过<br>“TXCACHENORTIME（发送缓存连续正常状态时长（ms））”<br>参数指定）则退出拥塞控制状态。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：10~65535<br>系统初始设置值：300<br>配置原则：<br>“发送缓存过载恢复时延（ms）”<br>的配置值应小于<br>“发送缓存过载时延（ms）”<br>的配置值。 |
| TXCACHENORTIME | 发送缓存连续正常状态时长（ms） | 可选必选说明：条件可选参数<br>参数含义：SCTP发送缓存处于正常状态时长超过此阈值，则退出流控。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：10~4294967295<br>系统初始设置值：10000 |
| TXCACHEOVLPER | 发送缓存过载比例门限（%） | 可选必选说明：条件可选参数<br>参数含义：SCTP发送缓存占用率大于该门限后进入拥塞控制状态，低优先级消息和高优先级消息均会被流控。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~99<br>系统初始设置值：80<br>配置原则：<br>“发送缓存过载比例门限（%）”<br>配置值应大于<br>“发送缓存过载恢复比例门限（%）”<br>配置值。 |
| TXCACHERESPER | 发送缓存过载恢复比例门限（%） | 可选必选说明：条件可选参数<br>参数含义：SCTP发送缓存占用率小于该门限后退出拥塞控制状态。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~99<br>系统初始设置值：60<br>配置原则：<br>“发送缓存过载恢复比例门限（%）”<br>配置值应小于<br>“发送缓存过载比例门限（%）”<br>配置值。 |
| STARTALARMTIMES | 告警上报周期数 | 可选必选说明：条件可选参数<br>参数含义：该参数用于设置连续几个1秒周期处于流控态时上报“ALM-80715 RAN侧SCTP层链路拥塞流控”告警。<br>前提条件：该参数在<br>“CCTRLSW（拥塞控制功能）”<br>配置为<br>“ON(开启)”<br>且<br>“CCTRLALGTYPE（拥塞控制算法）”<br>配置为<br>“BBR（BBR拥塞控制算法）”<br>后生效。<br>数据来源：本端规划<br>取值范围：1~60<br>系统初始设置值：10<br>配置原则：该参数设置过低会导致稳态运行时因部分基站链路拥塞而频繁触发“ALM-80715 RAN侧SCTP层链路拥塞流控”告警，设置过高会导致链路拥塞后长时间流控而不上报告警。<br>说明：软参<br>[DWORD_EX_B85 BIT7](../../../../../../../软件参数/UNC软件参数/业务软件参数/软件参数（SGSN_MME）/参数说明/SCTP管理/DWORD_EX_B85 BIT7 控制UNC是否上报RAN侧SCTP层链路拥塞流控告警_03112355.md)<br>可控制UNC是否上报“ALM-80715 RAN侧SCTP层链路拥塞流控”告警。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SCTPCCTRLPARA]] · RAN侧拥塞检测功能参数（SCTPCCTRLPARA）

## 使用实例

设置RAN侧拥塞检测功能参数，拥塞控制功能开启、拥塞控制算法为BBR、低优先级消息流控时延为300ms、高优先级消息流控时延为450ms、发送缓存过载时延为800ms、连续过载次数为5个、发送缓存过载恢复时延为300ms、发送缓存连续正常状态时长为10000ms、发送缓存过载比例门限为80%、发送缓存过载恢复比例门限为60%、告警上报周期数为10：

```
SET SCTPCCTRLPARA: CCTRLSW=ON, CCTRLALGTYPE=BBR, LOWOVLTHD=300, HIGHOVLTHD=450, TXCACHEOVLTHD=800, TXCACHEOVLNUM=5, TXCACHERESTHD=300, TXCACHENORTIME=10000, TXCACHEOVLPER=80, TXCACHERESPER=60, STARTALARMTIMES=10;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/SET-SCTPCCTRLPARA.md`
