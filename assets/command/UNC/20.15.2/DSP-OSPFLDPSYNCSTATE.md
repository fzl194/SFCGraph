---
id: UNC@20.15.2@MMLCommand@DSP OSPFLDPSYNCSTATE
type: MMLCommand
name: DSP OSPFLDPSYNCSTATE（查询OSPF LDP联动状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFLDPSYNCSTATE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF LDP联动状态信息
status: active
---

# DSP OSPFLDPSYNCSTATE（查询OSPF LDP联动状态信息）

## 功能

该命令用于查询OSPF LDP联动状态的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| IFNAME | 接口名 | 可选必选说明：可选参数<br>参数含义：接口名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63。<br>默认值：无<br>配置原则：请使用LST INTERFACE命令查看可用接口。 |

## 操作的配置对象

- [OSPF LDP联动状态信息（OSPFLDPSYNCSTATE）](configobject/UNC/20.15.2/OSPFLDPSYNCSTATE.md)

## 使用实例

查询OSPF进程1的LDP联动状态：

```
DSP OSPFLDPSYNCSTATE:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                     OSPF进程号  =  1
                         接口名  =  Ethernet64/0/7
          HoldDown时间间隔（s）  =  10
       HoldMaxCost时间间隔（s）  =  10
永久通告HoldMaxCost时间间隔标识  =  TRUE
                    LDP会话状态  =  ---
            LDP和OSPF的同步状态  =  HoldMaxCost
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF-LDP联动状态信息（DSP-OSPFLDPSYNCSTATE）_49801630.md`
