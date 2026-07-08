---
id: UDG@20.15.2@MMLCommand@LST LDPREMOTEPEER
type: MMLCommand
name: LST LDPREMOTEPEER（查询LDP远端邻居配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: LDPREMOTEPEER
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- MPLS管理
- LDP管理
- LDP远端邻居管理
status: active
---

# LST LDPREMOTEPEER（查询LDP远端邻居配置）

## 功能

该命令用于查询LDP远端邻居。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| VRFNAME | VPN实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示VPN实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无 |
| REMOTEPEERNAME | 远端邻居名 | 可选必选说明：可选参数<br>参数含义：该参数用于指定远端邻居名。配置LDP远端会话，需要指定远端邻居名和IP地址。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/LDPREMOTEPEER]] · LDP远端邻居（LDPREMOTEPEER）

## 使用实例

查询LDP远端邻居：

```
LST LDPREMOTEPEER:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
             VPN实例名称  =  _public_
              远端邻居名  =  r2
          远端邻居IP地址  =  192.168.1.3
         禁止发送mapping  =  FALSE
  Hello报文发送时间（s）  =  NULL
  Hello报文保持时间（s）  =  45
 KA报文发送间隔时间（s）  =  NULL
     KA报文保持时间（s）  =  45
    本地LSR ID绑定接口名  =  NULL
    IGP联动延迟时间（s）  =  10
            标签发布模式  =  DU
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-LDPREMOTEPEER.md`
