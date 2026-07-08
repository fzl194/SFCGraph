---
id: UNC@20.15.2@MMLCommand@DSP MASALMCHECK
type: MMLCommand
name: DSP MASALMCHECK（显示5G告警核查状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: MASALMCHECK
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 告警管理
- 告警核查
status: active
---

# DSP MASALMCHECK（显示5G告警核查状态）

## 功能

本命令用于查询系统当前的告警核查状态。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “HTTP_LINKDOWN（HTTP链路故障）”：表示ALM-100155 HTTP链路故障告警，对应的批量告警为ALM-100311 批量HTTP链路故障。<br>- “SUMMARY（汇总）”：表示批量告警的汇总信息。<br>默认值：SUMMARY<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/MASALMCHECK]] · 5G告警核查（MASALMCHECK）

## 使用实例

查询告警核查：

```
%%DSP MASALMCHECK: ALMTYPE=HTTP_LINKDOWN;%%
RETCODE = 0  操作成功

结果如下
--------
告警名称  =  HTTP链路故障
核查类型  =  无
核查状态  =  空闲
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-MASALMCHECK.md`
