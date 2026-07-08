---
id: UNC@20.15.2@MMLCommand@DSP PAEOVERLOADSTAT
type: MMLCommand
name: DSP PAEOVERLOADSTAT（显示PAE过载状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PAEOVERLOADSTAT
command_category: 查询类
applicable_nf:
- MME
- AMF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 业务流控管理
- PAE寻呼反压流控管理
status: active
---

# DSP PAEOVERLOADSTAT（显示PAE过载状态）

## 功能

**适用NF：MME、AMF**

此命令用于查询link-pod的PAE过载状态信息。

## 注意事项

此命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QRYTYPE | 查询类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定查询的link-pod范围。<br>取值范围：<br>- “ALL（全部）”<br>- “OVERLOAD（过载）”<br>默认值：“ALL（全部）” |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PAEOVERLOADSTAT]] · PAE过载状态（PAEOVERLOADSTAT）

## 使用实例

查询所有link-pod的PAE过载状态信息，可以使用如下命令：

DSP PAEOVERLOADSTAT: QRYTYPE=ALL;

```
%%DSP PAEOVERLOADSTAT: QRYTYPE=ALL;%%
RETCODE = 0  操作成功

操作结果如下:
-------------------------
POD名称          过载状态   过载原因   最近过载启动时间            最近过载结束时间

link-pod-0       正常       N/A        2022-03-22 17:59:32+08:00   2022-03-22 17:59:45+08:00
link-pod-1       正常       N/A        2000-01-01 00:00:00+08:00   2000-01-01 00:00:00+08:00     
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PAEOVERLOADSTAT.md`
