---
id: UDG@20.15.2@MMLCommand@DSP NPFABRICSUBHEALTHY
type: MMLCommand
name: DSP NPFABRICSUBHEALTHY（显示NP FABRIC亚健康信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPFABRICSUBHEALTHY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP Fabric链路管理
- NP亚健康状态
status: active
---

# DSP NPFABRICSUBHEALTHY（显示NP FABRIC亚健康信息）

## 功能

该命令用于显示NP Fabric平面亚健康信息。

## 注意事项

- 此命令显示两个资源之间的链路亚健康信息。
- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RESNAME | 源资源名称 | 可选必选说明：必选参数。<br>参数含义：该参数用于指定源资源名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，输入长度范围为1～128。不支持空格，区分大小写。<br>配置原则：FRAME-x-SLOT-y，区分大小写。其中x为框号，y为槽位号，可通过<br>[DSP NPNODE](../../../FEMF/NP状态查询（DSP NPNODE）_18818228.md)<br>查询。例：FRAME-0-SLOT-8表示0框8板。<br>默认值：无。 |

## 操作的配置对象

- [NP FABRIC亚健康信息（NPFABRICSUBHEALTHY）](configobject/UDG/20.15.2/NPFABRICSUBHEALTHY.md)

## 使用实例

显示资源名称为FRAME-0-SLOT-8的亚健康信息：

```
DSP NPFABRICSUBHEALTHY:RESNAME="FRAME-0-SLOT-8";
```

```
RETCODE = 0  操作成功

结果如下
--------
源资源名称      远端资源名称         源节点TB  远端节点TB  是否亚健康  亚健康值  

FRAME-0-SLOT-8  FRAME-0-SLOT-7-NP-0  1116      1115        FALSE       0        
FRAME-0-SLOT-8  FRAME-0-SLOT-8-NP-0  1112      1116        FALSE       0         
(结果个数 = 2)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示NP-FABRIC亚健康信息（DSP-NPFABRICSUBHEALTHY）_44203950.md`
