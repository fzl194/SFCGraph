---
id: UNC@20.15.2@MMLCommand@DSP OSPFLSDBSTATEINFO
type: MMLCommand
name: DSP OSPFLSDBSTATEINFO（查询OSPF LSDB的状态信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFLSDBSTATEINFO
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF LSDB的状态信息
status: active
---

# DSP OSPFLSDBSTATEINFO（查询OSPF LSDB的状态信息）

## 功能

该命令用于显示OSPF LSDB的状态信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| LSATYPE | LSA类型 | 可选必选说明：可选参数<br>参数含义：LSA类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- Router：Router LSA。<br>- Network：Network LSA。<br>- Sum_Net：ABR Summary LSA。<br>- Sum_Asbr：ASBR Summary LSA。<br>- External：AS-External LSA。<br>- NSSA：NSSA LSA。<br>- Opq_Link：Opaque Link LSA。<br>- Opq_Area：Opaque Area LSA。<br>- Opq_As：Opaque AS LSA。<br>默认值：无 |
| LINKSTATEID | LSA报头中的链路状态ID | 可选必选说明：可选参数<br>参数含义：LSA报头中的链路状态ID。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。点分十进制格式。<br>默认值：无 |

## 操作的配置对象

- [OSPF LSDB的状态信息（OSPFLSDBSTATEINFO）](configobject/UNC/20.15.2/OSPFLSDBSTATEINFO.md)

## 使用实例

显示OSPF进程1下LSDB的状态信息：

```
DSP OSPFLSDBSTATEINFO:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
               OSPF进程号  =  1
                   区域号  =  0.0.0.0
               路由器标识  =  192.168.3.111
                  LSA类型  =  Router LSA
    LSA报头中的链路状态ID  =  192.168.3.111
发布或产生LSA的路由器标识  =  192.168.3.111
            LSA的老化时间  =  74
                  LSA长度  =  36
                  LSA选项  =  E
                LSA序列号  =  0x80000001
                LSA校验和  =  0xa08c
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF-LSDB的状态信息（DSP-OSPFLSDBSTATEINFO）_50120670.md`
