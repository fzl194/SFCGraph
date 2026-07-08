---
id: UDG@20.15.2@MMLCommand@DSP NPPORTPODTBMAP
type: MMLCommand
name: DSP NPPORTPODTBMAP（显示NP卡和Pod TB出端口映射信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NPPORTPODTBMAP
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 系统管理
- NP端口管理
- NP卡和Pod TB出端口映射信息
status: active
---

# DSP NPPORTPODTBMAP（显示NP卡和Pod TB出端口映射信息）

## 功能

该命令用于显示NP卡和Pod TB出端口映射信息，其中包含NP卡内联口和CPU的连接关系、Pod TB出端口状态和刷新时间等附加信息。

## 注意事项

该命令仅适用于NP卡类型为NP121的加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CHASSISID | 框号 | 可选必选说明：可选参数。<br>参数含义：该参数表示NP卡连接的CPU上的Pod TB出端口所属框的编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为0～7。<br>配置原则：无。<br>默认值：无。 |
| SLOTID | 槽位号 | 可选必选说明：可选参数。<br>参数含义：该参数表示NP卡连接的CPU上的Pod TB出端口所属插槽的编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为1～8。<br>配置原则：无。<br>默认值：无。 |
| PODNAME | Pod名称 | 可选必选说明：可选参数。<br>参数含义：该参数表示NP卡连接的CPU上的Pod名称。<br>数据来源：本端规划。<br>取值范围：字符串类型，取值长度为1～127。<br>配置原则：无。<br>默认值：无。 |
| PODTB | Pod TB | 可选必选说明：可选参数。<br>参数含义：该参数表示NP卡连接的CPU上的Pod TB出端口的编号。<br>数据来源：本端规划。<br>取值范围：整数类型，取值范围为1～4000。<br>配置原则：无。<br>默认值：无。 |

## 操作的配置对象

- [NP卡和Pod TB出端口映射信息（NPPORTPODTBMAP）](configobject/UDG/20.15.2/NPPORTPODTBMAP.md)

## 使用实例

查询NP内的Pod TB为20的出端口信息：

```
%%DSP NPPORTPODTBMAP:PODTB=20;%%
RETCODE = 0  操作成功

结果如下
--------
     Pod名称  =  femu-pod-0
      Pod TB  =  20
        框号  =  0
      槽位号  =  5
        NP号  =  0
      端口号  =  1001
     CPU编号  =  CPU01
      有效性  =  1
      时间戳  =  1672531200 1740451614000
    附加信息  =  1[1 1672531200] 2[1 167253199] 3[1 167253198]
Tick变化信息  =  1[1672531200 2025-02-25 10:00:01] 2[167253199 2025-02-25 10:00:00] 3[167253198 2025-02-25 09:59:59]
(结果数量 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示NP卡和Pod-TB出端口映射信息（DSP-NPPORTPODTBMAP）_20420301.md`
