---
id: UDG@20.15.2@MMLCommand@DSP OSPFV3CUMULATIVE
type: MMLCommand
name: DSP OSPFV3CUMULATIVE（查询OSPFv3统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFV3CUMULATIVE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPFv3管理
- 查询OSPFv3统计信息
status: active
---

# DSP OSPFV3CUMULATIVE（查询OSPFv3统计信息）

## 功能

该命令用于显示OSPFv3统计信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | OSPFv3进程号 | 可选必选说明：可选参数<br>参数含义：OSPFv3进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/OSPFV3CUMULATIVE]] · OSPFv3统计信息（OSPFV3CUMULATIVE）

## 使用实例

显示OSPFv3进程1的统计信息：

```
DSP OSPFV3CUMULATIVE:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
------------------------
   OSPFv3进程号  =  1
     路由器标识  =  192.168.3.11
接收Hello包数目  =  175
发送Hello包数目  =  178
   接收DD包数目  =  0
   发送DD包数目  =  0
  接收LSR包数目  =  0
  发送LSR包数目  =  0
  接收LSU包数目  =  0
  发送LSU包数目  =  0
接收LSAck包数目  =  0
发送LSAck包数目  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFV3CUMULATIVE.md`
