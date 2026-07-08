---
id: UNC@20.15.2@MMLCommand@DSP PODHEALREC
type: MMLCommand
name: DSP PODHEALREC（查询POD重建历史记录）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PODHEALREC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 可靠性管理
- 微服务可靠性管理
status: active
---

# DSP PODHEALREC（查询POD重建历史记录）

## 功能

该命令用于查询POD重建历史记录。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PODNAME | POD名称 | 可选必选说明：可选参数<br>参数含义：该参数用于显示重建的POD名称。如果不输入该输出，则查询系统内所有POD的重建记录。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PODHEALREC]] · POD重建历史记录（PODHEALREC）

## 使用实例

查询POD重建历史记录。

```
%%DSP PODHEALREC:;%%
RETCODE = 0  操作成功

结果如下
--------
        序号  =  1
     POD名称  =  vsm-pod-54ddc977b9-4g42g
      堆栈ID  =  524c409a-bc3b-11ea-a186-025565660064
       PodID  =  c2208db2-bc3b-11ea-9d1b-fa163eb94edd
故障容器类型  =  ContainerSm
    故障类型  =  反复故障
故障发生时间  =  2020-07-09 09:06:10
    重建时间  =  2020-07-09 09:08:03+00:00
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PODHEALREC.md`
