---
id: UDG@20.15.2@MMLCommand@DSP OSPFHOSTTABLE
type: MMLCommand
name: DSP OSPFHOSTTABLE（查询OSPF动态主机名的信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: OSPFHOSTTABLE
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 路由管理
- OSPF管理
- 查询OSPF动态主机名的信息
status: active
---

# DSP OSPFHOSTTABLE（查询OSPF动态主机名的信息）

## 功能

该命令用于显示OSPF动态主机名的信息。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCID | 进程号 | 可选必选说明：可选参数<br>参数含义：OSPF进程号。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～4294967295。<br>默认值：无 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@OSPFHOSTTABLE]] · OSPF动态主机名的信息（OSPFHOSTTABLE）

## 使用实例

查看OSPF进程1的动态主机名信息：

```
DSP OSPFHOSTTABLE:PROCID=1;
```

```

RETCODE = 0  操作成功。

结果如下
-------------------------
            进程号  =  1
            区域号  =  0.0.0.0
        动态主机名  =  HostName
        路由器标识  =  192.168.7.1
自治域洪泛的主机名  =  区域范围
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-OSPFHOSTTABLE.md`
