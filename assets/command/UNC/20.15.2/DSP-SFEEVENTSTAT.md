---
id: UNC@20.15.2@MMLCommand@DSP SFEEVENTSTAT
type: MMLCommand
name: DSP SFEEVENTSTAT（显示SFE事件统计信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SFEEVENTSTAT
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- 统计信息
status: active
---

# DSP SFEEVENTSTAT（显示SFE事件统计信息）

## 功能

该命令用于显示SFE事件统计信息。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUNAME | RU名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定资源单元名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：<br>- 区分大小写，不支持空格。<br>- 使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SFEEVENTSTAT]] · SFE事件统计信息（SFEEVENTSTAT）

## 使用实例

显示指定资源单元上的SFE事件计数信息：

```
DSP SFEEVENTSTAT:RUNAME="VNODE_VNRS_VNFC_IPU_0064";
```

```

RETCODE = 0  操作成功

结果如下
-------------------------
RU名称                      事件类型                      报文计数 

VNODE_VNRS_VNFC_IPU_0064    VFP_CAUSE_EVENT_ARP_MISS      0             
VNODE_VNRS_VNFC_IPU_0064    VFP_CAUSE_EVENT_BFD_MSG       0
VNODE_VNRS_VNFC_IPU_0064    VFP_CAUSE_EVENT_MPLSARP_MISS  0           
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SFEEVENTSTAT.md`
