---
id: UDG@20.15.2@MMLCommand@DSP OSPFLASTDOWNNBR
type: MMLCommand
name: DSP OSPFLASTDOWNNBR（查询OSPF上次Down的邻居）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFLASTDOWNNBR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF Down的邻居信息
status: active
---

# DSP OSPFLASTDOWNNBR（查询OSPF上次Down的邻居）

## 功能

该命令用于显示OSPF断开的邻居信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFLASTDOWNNBR]] · OSPF上次Down的邻居（OSPFLASTDOWNNBR）

## 使用实例

显示设备OSPF进程号为1的所有断开的路由信息：

```
DSP OSPFLASTDOWNNBR: PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
             进程号  =  1
         路由器标识  =  192.168.2.2
       邻居区域标识  =  0.0.0.0
             接口名  =  Ethernet64/0/3
         邻居IP地址  =  192.168.2.1
     邻居路由器标识  =  192.168.2.1
 邻居Down的直接原因  =  邻居状态Down由于非活跃记时器被激活
 邻居Down的次要原因  =  邻居状态Down由于未收到Hello包
     邻居Down的时间  =  2016-03-14 10:54:33

(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFLASTDOWNNBR.md`
