---
id: UNC@20.15.2@MMLCommand@DSP PAEFABDETBRF
type: MMLCommand
name: DSP PAEFABDETBRF（显示Fabric链路探测简要结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEFABDETBRF
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统调测
- PAE 调测命令
- 链路探测
status: active
---

# DSP PAEFABDETBRF（显示Fabric链路探测简要结果）

## 功能

该命令用于查询Fabric平面链路状态探测简要结果。

## 注意事项

探测任务中执行命令只支持查询目的端探测结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCPODNAME | 源Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| DSTPODNAME | 目的Pod名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端Pod名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP POD**](../../../操作维护/Pod管理/POD查询（DSP POD）_69830277.md)<br>获取Pod名称。 |
| SRCPORTNAME | 源端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定本端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |
| DSTPORTNAME | 目的端口名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定远端端口名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~20。<br>默认值：无<br>配置原则：<br>使用<br>[**DSP PAEPORTINFO**](../端口/显示PAE端口基本信息（DSP PAEPORTINFO）_92520040.md)<br>获取探测端口名称（仅支持Fabric端口）。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEFABDETBRF]] · Fabric链路探测简要结果（PAEFABDETBRF）

## 使用实例

显示Fabric链路探测简要结果：

```
+++    UNC/*MEID:0 MENAME:UNC_z30062954_X86_20241226_1001*/        2024-12-26 15:59:46
O&M    #3308
%%DSP PAEFABDETBRF: SRCPODNAME="cslbip-pod-0", DSTPODNAME="vup-pod-0", SRCPORTNAME="eth2", DSTPORTNAME="eth2";%%
RETCODE = 0  操作成功

结果如下
--------
Pod名称       探测类型   发送报文数  接收报文数  

cslbip-pod-0  源端Pod    159         159         
vup-pod-0     目的端Pod  159         159         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示Fabric链路探测简要结果（DSP-PAEFABDETBRF）_12631724.md`
