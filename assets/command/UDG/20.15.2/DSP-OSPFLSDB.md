---
id: UDG@20.15.2@MMLCommand@DSP OSPFLSDB
type: MMLCommand
name: DSP OSPFLSDB（查询OSPF链接状态数据库）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFLSDB
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF链接状态数据库
status: active
---

# DSP OSPFLSDB（查询OSPF链接状态数据库）

## 功能

该命令用于显示OSPF的链路状态数据库LSDB信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| AREAID | 区域标识 | 可选必选说明：可选参数<br>参数含义：区域标识。<br>数据来源：对端协商<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [OSPF链接状态数据库（OSPFLSDB）](configobject/UDG/20.15.2/OSPFLSDB.md)

## 使用实例

显示设备OSPF进程号为1的所有链路状态数据库信息：

```
DSP OSPFLSDB: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
                 进程号  =  1
         本地路由器标识  =  192.168.7.1
               区域标识  =  0.0.0.0
        末梢区域LSA数量  =  0
         Router-LSA数量  =  2
        Network-LSA数量  =  1
Summary Network LSA数量  =  0
           ASBR LSA数量  =  0
             7类LSA数量  =  0
             9类LSA数量  =  0
            10类LSA数量  =  0
            11类LSA数量  =  0
            ASE LSA数量  =  0
                   总数  =  3
           自治区域范围  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询OSPF链接状态数据库（DSP-OSPFLSDB）_00601289.md`
