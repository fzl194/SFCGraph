---
id: UDG@20.15.2@MMLCommand@DSP OSPFMAXAGELSA
type: MMLCommand
name: DSP OSPFMAXAGELSA（查询OSPF MaxAge LSA信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFMAXAGELSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF MaxAge LSA的信息
status: active
---

# DSP OSPFMAXAGELSA（查询OSPF MaxAge LSA信息）

## 功能

该命令用于查询当前设备中达到最大老化时间的Router LSA或收到远端flush的Router LSA的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPF MaxAge LSA信息（OSPFMAXAGELSA）](configobject/UDG/20.15.2/OSPFMAXAGELSA.md)

## 使用实例

查询OSPF进程1中达到最大老化时间或收到远端flush的Router LSA的信息：

```
DSP OSPFMAXAGELSA:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                   进程号  =  1
                   区域号  =  0.0.0.0
               路由器标识  =  10.10.10.1
    LSA报头中的链路状态ID  =  10.10.10.1
  LSA时限达到MaxAge的次数  =  0
  LSA上次达到MaxAge的时间  =  NULL
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF-MaxAge-LSA信息（DSP-OSPFMAXAGELSA）_50281670.md`
