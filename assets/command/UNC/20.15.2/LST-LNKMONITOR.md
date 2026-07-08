---
id: UNC@20.15.2@MMLCommand@LST LNKMONITOR
type: MMLCommand
name: LST LNKMONITOR（查询链路频繁闪断监控配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LNKMONITOR
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
- 接口链路调测
status: active
---

# LST LNKMONITOR（查询链路频繁闪断监控配置）

## 功能

**适用网元：SGSN、MME**

本命令用于查询链路频繁闪断监控功能的参数配置。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LNKTYPE | 链路类型 | 可选必选说明：可选参数<br>参数含义：本参数用于指定待查询的链路类型。<br>数据来源：本端规划<br>取值范围：<br>“S1AP(S1AP 链路)” |

## 操作的配置对象

- [链路频繁闪断监控配置（LNKMONITOR）](configobject/UNC/20.15.2/LNKMONITOR.md)

## 使用实例

查询 “链路类型” 为 “S1AP(S1AP 链路)” 时，链路频繁闪断的监控和告警上报的参数配置：

LST LNKMONITOR: LNKTYPE=S1AP;

```
%%LST LNKMONITOR: LNKTYPE=S1AP;%%
RETCODE = 0  操作成功。

操作结果如下
------------
瞬间闪断监控开关  =  开启
   统计时长（s）  =  60
        统计门限  =  50
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询链路频繁闪断监控配置（LST-LNKMONITOR）_72225541.md`
