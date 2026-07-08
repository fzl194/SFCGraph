---
id: UNC@20.15.2@MMLCommand@LST ALMRPTMODE
type: MMLCommand
name: LST ALMRPTMODE（查询告警上报模式）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: ALMRPTMODE
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
- 操作维护
- 告警管理
- 告警上报模式
status: active
---

# LST ALMRPTMODE（查询告警上报模式）

## 功能

**适用网元：SGSN、MME**

该命令用于查询告警上报模式及相关参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ALMTYPE | 告警类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定告警类型。<br>数据来源：本端规划<br>取值范围：<br>- “S1apLinkDown(S1ap链路故障)”<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/ALMRPTMODE]] · 告警上报模式（ALMRPTMODE）

## 使用实例

查询系统中，S1ap链路故障的告警上报模式：

LST ALMRPTMODE: ALMTYPE=S1apLinkDown;

```
%%LST ALMRPTMODE: ALMTYPE=S1apLinkDown;%%
RETCODE = 0  操作成功。

操作结果如下
------------
         告警类型  =  S1ap链路故障
 批量告警上报开关  =  开
批量统计周期（s）  =  60
     批量统计门限  =  100
 原始告警上报开关  =  关
     批量恢复门限  =  0
 批量恢复百分比(%) =  10
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询告警上报模式(LST-ALMRPTMODE)_72225883.md`
