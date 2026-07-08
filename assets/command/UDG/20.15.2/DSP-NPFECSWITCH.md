---
id: UDG@20.15.2@MMLCommand@DSP NPFECSWITCH
type: MMLCommand
name: DSP NPFECSWITCH（查询NP FEC状态）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPFECSWITCH
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP端口FEC功能启停
- NP板的FEC功能开关
status: active
---

# DSP NPFECSWITCH（查询NP FEC状态）

## 功能

该命令用于查询NP端口FEC状态信息。

## 注意事项

- 该命令仅适用于NP卡加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| RUID | RU编号 | 可选必选说明：必选参数。<br>参数含义：RU编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～4294967294。<br>配置原则：使用<br>[DSP RU](../../../../../单体服务公共功能管理/系统管理/资源管理/RU管理/显示资源单元信息（DSP RU）_59103857.md)<br>命令查询RU编号。<br>默认值：无。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NPFECSWITCH]] · NP FEC状态（NPFECSWITCH）

## 使用实例

查询RUID为66的NP卡端口FEC状态信息：

```
DSP NPFECSWITCH:RUID=66;
```

```
RETCODE = 0  操作成功

结果如下
--------
接口名称     NP端口名称    FEC 状态     附加信息  

100GE66/0/6  100G/NP0/0    NP_FEC_NONE  P4        
100GE66/0/7  100G/NP0/130  NP_FEC_NONE  P3        
100GE66/0/8  100G/NP0/4    NP_FEC_NONE  P2        
100GE66/0/9  100G/NP0/134  NP_FEC_NONE  P1        
25GE66/0/10  25G/NP0/8     FEC_MOD_RS   P6        
25GE66/0/11  25G/NP0/138   FEC_MOD_RS   P5        
25GE66/0/12  25G/NP0/9     FEC_MOD_RS   P8        
25GE66/0/13  25G/NP0/139   FEC_MOD_RS   P7        
(结果个数 = 8)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询NP-FEC状态（DSP-NPFECSWITCH）_71467900.md`
