---
id: UNC@20.15.2@MMLCommand@DSP OSPFERRORLSA
type: MMLCommand
name: DSP OSPFERRORLSA（查询OSPF错误LSA的信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: OSPFERRORLSA
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- OSPF错误LSA信息
status: active
---

# DSP OSPFERRORLSA（查询OSPF错误LSA的信息）

## 功能

该命令用于查询OSPF错误LSA的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPF进程号 | 可选必选说明：可选参数<br>参数含义：该参数用于表示OSPF进程号，未指定OSPF进程号时默认查询所有OSPF进程。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/OSPFERRORLSA]] · OSPF错误LSA的信息（OSPFERRORLSA）

## 使用实例

查询OSPF错误LSA的信息：

```
DSP OSPFERRORLSA:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
        OSPF进程号  =  1
        路由器标识  =  192.168.1.1
LSA的失效时长（s）  =  1
       LSA的选项域  =  2
         LSA的类型  =  Router-LSA
       LSA的状态ID  =  192.168.2.50
        发布路由器  =  192.168.2.50
         LSA的序号  =  0x80000041
       LSA的校验值  =  0xc4f5
         LSA的长度  =  36
 接收LSA的接口名称  =  Ethernet66/0/7
     接收LSA的时间  =  2017-10-24 12:01:51
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询OSPF错误LSA的信息（DSP-OSPFERRORLSA）_00440385.md`
