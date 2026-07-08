---
id: UDG@20.15.2@MMLCommand@DSP SFETRACESTC
type: MMLCommand
name: DSP SFETRACESTC（查询SFE跟踪报文统计）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: SFETRACESTC
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- 转发引擎实例FEI
- SFE跟踪报文统计
status: active
---

# DSP SFETRACESTC（查询SFE跟踪报文统计）

## 功能

该命令用来查询SFE跟踪报文统计。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKID | 跟踪任务ID | 可选必选说明：必选参数<br>参数含义：该参数用于指定跟踪任务ID，可用DSP TRCTASK进行查询。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0～4294967295。<br>默认值：无 |
| RUNAME | 资源单元名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定资源单元名称，可用DSP RU进行查询。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。区分大小写。<br>默认值：无<br>配置原则：使用DSP RU查看RU名称。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/SFETRACESTC]] · SFE跟踪报文统计（SFETRACESTC）

## 使用实例

查询SFE跟踪报文统计：

```
DSP SFETRACESTC:RUNAME="VNODE_VNRS_VNFC_IPU_0065",TASKID=8;
```

```
 
RETCODE = 0  操作成功。

结果如下
------------------------
符合条件的报文  =  28
跟踪上报的报文  =  28
  重定向的报文  =  0
    丢弃的报文  =  0
  跟踪报文类型  =  ARP
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询SFE跟踪报文统计（DSP-SFETRACESTC）_00601145.md`
