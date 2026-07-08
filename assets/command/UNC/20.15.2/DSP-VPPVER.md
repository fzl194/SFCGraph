---
id: UNC@20.15.2@MMLCommand@DSP VPPVER
type: MMLCommand
name: DSP VPPVER（显示组件版本）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: VPPVER
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 扩展调测
- 业务调测
- VPPVER
status: active
---

# DSP VPPVER（显示组件版本）

## 功能

**适用网元：SGSN、MME**

此命令用于查看产品使用SS7组件的版本信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定SPU资源单元名。该参数可以通过<br>[DSP RU](../../../../../../平台服务管理/单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询。<br>取值范围：0~63 位字符串<br>默认值：无 |
| PT | 进程类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程的进程类型。<br>取值范围：<br>- SPP(SPP)<br>- SGP(SGP)<br>默认值：无 |
| PN | 进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于指定进程号。<br>取值范围：0～20<br>默认值：无 |
| VPPT | 组件类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定查询的组件类型。<br>取值范围：<br>- “M3UA(M3UA)”<br>- “SCTP(SCTP)”<br>- “TCAP(TCAP)”<br>- “SCCP(SCCP)”<br>默认值：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VPPVER]] · 组件版本（VPPVER）

## 使用实例

查询组件M3UA的版本：

DSP VPPVER: VPPT=M3UA;

```
%%DSP VPPVER: VPPT=M3UA;%%
RETCODE = 0  操作成功。

查询组件版本
------------
组件类型  =  M3UA
组件版本  =  VPP V300R003C26SPC220 (M3UA) (RFC3332)       [10:33:49]
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-VPPVER.md`
