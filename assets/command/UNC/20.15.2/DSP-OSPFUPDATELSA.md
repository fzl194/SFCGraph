---
id: UNC@20.15.2@MMLCommand@DSP OSPFUPDATELSA
type: MMLCommand
name: DSP OSPFUPDATELSA（查询OSPF接收的LSA的更新信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFUPDATELSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF更新LSA信息
status: active
---

# DSP OSPFUPDATELSA（查询OSPF接收的LSA的更新信息）

## 功能

该命令用于查询OSPF接收的LSA的更新信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ISBRIEF | 是否是简要信息 | 可选必选说明：必选参数<br>参数含义：该参数用来表示输出是否是LSA更新的简要信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- FALSE：输出LSA更新的详细信息。<br>- TRUE：输出LSA更新的简要信息。<br>默认值：无 |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示OSPF进程号，未指定OSPF进程号时默认查询所有OSPF进程。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |
| HISTORYFLAG | 查询信息类型 | 可选必选说明：条件必选参数<br>前提条件：该参数在“ISBRIEF”配置为“FALSE”时为必选参数。<br>参数含义：该参数用于表示是否查询历史信息。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- ORIGINATE-ROUTER：查看路由信息选项。<br>- HISTORY：配置查看历史信息选项。<br>默认值：无 |
| ADVRTRID | 发布路由器 | 可选必选说明：条件必选参数<br>前提条件：该参数在“HISTORYFLAG”配置为“ORIGINATE-ROUTER”时为必选参数。<br>参数含义：该参数用于表示发布LSA的路由器。<br>数据来源：本端规划<br>取值范围：IPv4地址类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFUPDATELSA]] · OSPF接收的LSA的更新信息（OSPFUPDATELSA）

## 使用实例

查询OSPF接收的LSA的更新信息：

```
DSP OSPFUPDATELSA:ISBRIEF=FALSE,HISTORYFLAG=ORIGINATE-ROUTER,ADVRTRID="192.168.1.1";
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
                      OSPF进程号  =  1
                      路由器标识  =  10.10.10.10
                      发布路由器  =  192.168.1.1
                   LSA更新总次数  =  2
                最后一次更新时间  =  2017-11-28 09:00:54
                统计计数开始时间  =  2017-11-28 08:44:56
                      记录的编号  =  0
         Router类型LSA的更新次数  =  1
        Network类型LSA的更新次数  =  1
Network Summary类型LSA的更新次数  =  0
   ASBR Summary类型LSA的更新次数  =  0
    AS External类型LSA的更新次数  =  0
         Type-7类型LSA的更新次数  =  0
         Type-9类型LSA的更新次数  =  0
        Type-10类型LSA的更新次数  =  0
        Type-11类型LSA的更新次数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-OSPFUPDATELSA.md`
