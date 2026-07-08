---
id: UDG@20.15.2@MMLCommand@DSP OSPFV3LSDB
type: MMLCommand
name: DSP OSPFV3LSDB（查询OSPFv3链接状态数据库）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFV3LSDB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3链接状态数据库
status: active
---

# DSP OSPFV3LSDB（查询OSPFv3链接状态数据库）

## 功能

该命令用于显示OSPFv3的链路状态数据库LSDB信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [OSPFv3链接状态数据库（OSPFV3LSDB）](configobject/UDG/20.15.2/OSPFV3LSDB.md)

## 使用实例

显示设备OSPFv3进程号为1的所有链路状态数据库信息：

```
DSP OSPFV3LSDB: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
    OSPFv3进程号  =  1
  本地路由器标识  =  10.1.1.1
  Router-LSA数量  =  2
 Network-LSA数量  =  1
 Summary-LSA数量  =  0
    ASBR LSA数量  =  0
   类型7 LSA数量  =  0
     ASE-LSA数量  =  0
    Link LSA数量  =  2
   Grace LSA数量  =  0
     未知LSA数量  =  0
内部区域前缀计数  =  1
   RiLinkLSA总数  =  0
   RiAreaLSA总数  =  0
     RiASLSA总数  =  0
        总的数量  =  6
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPFv3链接状态数据库（DSP-OSPFV3LSDB）_00865617.md`
