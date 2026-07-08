---
id: UNC@20.15.2@MMLCommand@DSP NODEINFO
type: MMLCommand
name: DSP NODEINFO（显示节点信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NODEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 系统管理
- 版本信息
status: active
---

# DSP NODEINFO（显示节点信息）

## 功能

该命令根据指定网元ID和类型查询节点的导出信息。若要获取最新的节点信息，请先使用EXP NODEINFO导出信息，再通过该命令查询导出的信息。

## 注意事项

- 该命令返回的信息为EXP NODEINFO的导出信息，若不执行EXP NODEINFO，则其返回信息不会发生变化。
- 若执行命令后的返回码为66348，则表示未导出过节点信息，请先使用EXP NODEINFO导出信息。
- 裸机容器场景不支持VF驱动的检查。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MEID | 网元ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定网元来查询节点信息；若不输入，则表示当前控制节点所在网元；网元ID可以通过LST ME命令查询出来。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| QUERYTYPE | 查询类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定需要查询信息的类型。<br>数据来源：本端规划<br>取值范围：<br>- VF_DRIVER（VF驱动）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [节点信息（NODEINFO）](configobject/UNC/20.15.2/NODEINFO.md)

## 使用实例

查询网元ID为0，查询类型为VF驱动的节点信息。 DSP NODEINFO: MEID=0, QUERYTYPE=VF_DRIVER;

```
%%DSP NODEINFO: MEID=0, QUERYTYPE=VF_DRIVER;%%
RETCODE = 0  操作成功。

结果如下
--------
网元ID 查询类型    节点IP        节点信息             

0      VF Driver   10.19.17.144  mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.89   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.168  空                  
0      VF Driver   10.19.17.60   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.25   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.191  mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.43   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.46   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.11   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.76   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.67   mlx4_en:4.4-2.0.7.0
  
0      VF Driver   10.19.17.44   mlx4_en:4.4-2.0.7.0

(结果个数 = 12)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示节点信息（DSP-NODEINFO）_94730419.md`
